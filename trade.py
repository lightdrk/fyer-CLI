import json
import os
import argparse
from colorama import Fore
from getpass import getpass
from helper import generate
from helper import refresh , orderTemplate
from datetime import datetime, timedelta
from helper.fyers_call import Authentication, order , Modify, Quote , orderHistory ,cancel



typeValue = {"limit":1,"Limit":1,"LIMIT":1,"market":2,"MARKET":2,"Market":2,"stoporder":3,"stopOrder":3,"STOPORDER":3,"stoplimit":4,"StopLimit":4,"STOPLIMIT":4}

#checks for needed option
def OrderOptionCheck():
    if args.symbol == None:
        exit(Fore.RED + "Refer to manual , usage using -h OR --help")
    if args.qty == None:
        exit(Fore.RED + "Refer to manual , usage using -h OR --help")
    if args.type == None:
        exit(Fore.RED + "'type' option needs value Refer to manual")
    if args.validity == None:
        exit(Fore.RED +"'validity' option needs value Refer to manual")

def refresIt():

    file_path = os.path.join(os.getcwd(),"helper/fyers_call/fyerSave.json")
    if os.path.exists(file_path):
        modified_time = os.path.getmtime(file_path)
        modified_datetime = datetime.fromtimestamp(modified_time)
        current_datetime = datetime.now()
        time_difference = current_datetime - modified_datetime
        minutes = time_difference.total_seconds() / 60
        return minutes
    else:
        return -1



if __name__ == '__main__':
    usage='''%(prog)s <command> [options]

    Commands:
    1. --gen                            Generate something
    2. <symbol> <product> <validity> [--qty <QTY> --type <TYPE> --buy/--sell]       order placement.
    3. --modify <orderId> [--qty <QTY> --type <TYPE> --limitPrice <PRICE> --stopPrice <PRICE>]   modifing order.
    4. --quote <symbol>                 returns quotes & market depth.
    5. --history <orderID>|--history    specific or history | retrives orders placed current trading day.              
    6. --cancel <orderID>               to cancel an order.

    Options:
    --qty <QTY>                     Specify quantity.
    --type <TYPE>                   Specify order type.
    --buy                           Buy option.
    --sell                          Sell option.
    --limitPrice <PRICE>            Specify limit price.
    --stopPrice <PRICE>             Specify stop price.
    --offlineOrder                  Include it for When placing AMO order.
    --disclosed                     disclosedQty Allowed only for Equity.

    Choices & Discription:
    1. <product>   ["CNC","INTRADAY","MARGIN","CO","BO"]   CNC => For equity only
                                                            INTRADAY => Applicable for all segments.
                                                            MARGIN => Applicable only for derivatives
                                                            CO => Cover Order
                                                            BO => Bracket Order
    
    2. <validity>    ["IOC","DAY"]                          IOC => Immediate or Cancel
                                                            DAY => Valid till the end of the day

    3. --offlineOrder ["True", "False"]                     False => When market is open
                                                            True => When placing AMO order
                            
    4. --type                                               1 => Limit Order
                                                            2 => Market Order
                                                            3 => Stop Order (SL-M)
                                                            4 => Stoplimit Order (SL-L)

    5. --limitPrice                                         Default => 0
                                                            Provide valid price for Limit and Stoplimit orders
                                                            *leave empty if dont want to use 
    
    6. --stopPrice                                          Default => 0
                                                            Provide valid price for Stop and Stoplimit orders
                                                            *leave empty if dont want to use .
                                                            
    7. --disclosed                                          disclosedQty*
                                                            Default => 0
                                                            Allowed only for Equity
                                                            *leave empty if dont want to use 
    
    8. --stopLoss                                           Default => 0
                                                            Provide valid price for CO and BO orders

    9. --takeProfit                                         Default => 0
                                                            Provide valid price for BO orders
    
    10. --buy                                               *does't need value

    11. --sell                                              *does't need value


    '''
    parser = argparse.ArgumentParser(prog="Trade_cli", usage=usage)
    
    group = parser.add_mutually_exclusive_group(required=False)
    group1 = parser.add_mutually_exclusive_group(required=True)  


    #generating everything first time
    group1.add_argument("-gen","--generate",action="store_true",default=None,help="for generating new auth_code and access token")

    group1.add_argument('symbol',nargs='?',help="Example: '[symbol] NSE:SBIN-EQ' OR '-s NSE:SBIN-EQ'")
    
    group1.add_argument('--modify',nargs='?',help="Example: 'orderID --type --qty --limit(limitPrice)/--stop(stopLoss)' OR 'orderID --type Limit --qty 100 --limit 12.12'")

    group1.add_argument('--quote',nargs='?',help="Example: --quote [symbol]")

    group1.add_argument('--history',nargs='?',const=True,default=None,action='store',help="Example: --history orderId OR --history")

    group1.add_argument('--cancel',nargs='?',help="Example: --cancel <orderId>")

    parser.add_argument('product',nargs='?',choices=["CNC","INTRADAY","MARGIN","CO","BO"] ,help="Example: '[product] CNC'")
    
    parser.add_argument('validity',nargs='?',choices=["IOC","DAY"],help="Example: '[validity] IOC'")
    
    parser.add_argument('--qty',nargs='?', help="Example: '--qty [quantity] 100'",type=int)
    parser.add_argument('--type',nargs='?',choices=["limit","Limit","LIMIT","market","MARKET","Market","stoporder","stopOrder","STOPORDER","stoplimit","StopLimit","STOPLIMIT"],help="Example: '[type] limit'",type=str)
    group.add_argument('--buy', action='store_true', help='Buy option')
    group.add_argument('--sell', action='store_true', help='Buy option')

  
    parser.add_argument('--offlineOrder',default="False",help="Example: '--offlineOrder True'",choices=["True","False"])
    parser.add_argument('--stopLoss',default=0,help="Example: '--stopLoss 12.12'")
    parser.add_argument('--takeProfit',default=0,help="Example: '--takeProfit 12.5'")
    parser.add_argument('--limitPrice',default=0, help="Example: '--limit 12.1'",type=float)
    parser.add_argument('--stopPrice',default=0, help="Example: '--stop 1222.1'",type=float)
    parser.add_argument('--disclosed',default=0, help="Example: '--disclosed 12" ,type=int)
    
    
    args = parser.parse_args()
    timeIn = refresIt()
    if timeIn > 1000:
        pin = getpass("your pin : ")
        refresh.new_access_token(pin)

    if args.generate:
        generate.gen()
    elif args.modify:
        data={"id":args.modify}
        if args.limitPrice:
            data["limitPrice"] = args.limitPrice
        if args.stopPrice:
            data["stopPrice"] = args.stopPrice
        if args.type:
            data["type"] = typeValue[args.type]
        if args.qty:
            data["qty"] = args.qty
        print(data)
        response = Modify.modify(data)
        print(response)
    elif args.quote:
        data = {"symbols":args.quote}
        print(Fore.BLUE + args.quote)
        quotes,Market_depth = Quote.quote(data)
        print(Fore.GREEN+ f'-------------------------------------------------------QUOTE---------------------------------------------------------------------------\n{quotes}')
        print(f'--------------------------------------------------Market_depth---------------------------------------------------------------------------------\n{Market_depth}')
    elif args.history:
        if isinstance(args.history,str):
            print(Fore.BLUE + args.history)
            print(Fore.GREEN+ '-------------------------------------------------------orderBook==OrderID---------------------------------------------------------------------------\n')
            print(orderHistory.OrderHistory(args.history))
                        
        else:
            print(Fore.GREEN+ '-------------------------------------------------------orderBook---------------------------------------------------------------------------\n')
            orderBook_response = orderHistory.orderBook()
            orderTemplate.template(orderBook_response)
    elif args.cancel:
        data = {"id": args.cancel}
        cancel_response = cancel.Cancel(data)
        print(cancel_response)
        if cancel_response['s'] == 'ok':
            print('============SUCESS===========')
        else:
            print(Fore.RED + cancel_response['message'])
    else:
        OrderOptionCheck()
        if args.buy or args.sell:
            if args.buy:
                value = 1
            else:
                value = -1
                
        else:
            parser.error('any of the buy OR sell needed')
        data = {
        "symbol": args.symbol, 
        "qty": args.qty,
        "type": typeValue[args.type],
        "side": value,
        "productType": args.product,
        "limitPrice": args.limitPrice,
        "stopPrice": args.stopPrice,
        "validity": args.validity,
        "disclosedQty": args.disclosed,
        "offlineOrder": args.offlineOrder,
        }
        print(data)
        revert = order.send(data)
        print(Fore.GREEN + f"{revert['message']}, {revert['id']}")
