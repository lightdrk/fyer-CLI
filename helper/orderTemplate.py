from colorama import Fore

def template(orderBook_response):
    status = { 1:'Canceled', 2:'Traded/Filled',3:'NaN',4:'Transit',5:'Rejected',6:'Pending',7:'Expired'}
    typeValue = {1:"Limit",2:"market",3:"stopOrder",4:"StopLimit"}
    segment = {10:'Equity',11:'F&O',12:'Currency',20:'Commodity'}
    side = {1:'buy', -1:'sell'}
    temp={}
    if len(orderBook_response['orderBook']) == 0:
        print(orderBook_response)
    for n in orderBook_response['orderBook']:
        n['type'] = typeValue[n['type']]
        n['segment'] = segment[n['segment']]
        n['side'] = side[n['side']]
        temp.setdefault(n['status'],[]).append(n)
    
    for n in temp:
        print(Fore.BLUE+f' ****************************  {status[n]}   ***********************           ')
        for order in temp[n]:
            print()
            print(Fore.GREEN+str(order))
    
