from fyers_api import fyersModel
import json
import os

# retrieves the full market quotes and market depth for symbols provided by the user.
def quote(data):
    with open(os.path.join(os.getcwd(),'helper/fyers_call/fyerSave.json'),'r') as saves:
        needed = json.load(saves)
    client_id = needed['client_id']
    access_token = needed['access_token']
    logs = os.path.join(os.getcwd(),'logs/quote')
    
    fyers = fyersModel.FyersModel(client_id=client_id,token=access_token,log_path=logs)

    quote_response = fyers.quotes(data=data)
    # removes 'symbols' and places its value in 'symbol'
    data['symbol'] = data.pop('symbols')

    if 'EQ' in data['symbol']:
        data["ohlcv_flag"] = 1

    depth_response = fyers.depth(data=data)

    return quote_response, depth_response
    
