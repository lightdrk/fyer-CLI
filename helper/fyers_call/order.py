from fyers_api import fyersModel
import json
import os


def send(data):
    with open(os.path.join(os.getcwd(),'helper/fyers_call/fyerSave.json'),'r') as saves:
        needed = json.load(saves)
    client_id = needed['client_id']
    access_token = needed['access_token']
    logs = os.path.join(os.getcwd(),'logs/orders')
    
    fyers = fyersModel.FyersModel(client_id=client_id,token=access_token,log_path=logs)

    response = fyers.place_order(data=data)
    return response