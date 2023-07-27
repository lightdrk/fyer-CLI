from fyers_api.Websocket import ws
from datetime import datetime, timedelta
from colorama import Fore, Back, Style
from helper import refresh
from getpass import getpass
import json
import os 


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

def run_process_symbol_data(access_token):
    data_type = "symbolData"
    with open(os.path.join(os.getcwd(),'config/marketdata.conf'),'r') as config:
        conf = json.load(config)
    symbol = conf['symbol']
    time = conf['time']
    fs = ws.FyersSocket(access_token=access_token,run_background=False,log_path="")
    fs.websocket_data = custom_message
    fs.subscribe(symbol=symbol,data_type=data_type)
    while True:
        fs.keep_running()
        time.sleep(time)


def custom_message(msg):
    print(Back.WHITE+Fore.RED+f"{msg[0]['symbol']}                   time:{datetime.now()}",Style.RESET_ALL)
    print (Fore.GREEN+f" message{msg}") 


def main():
    with open(os.path.join(os.getcwd(),'helper/fyers_call/fyerSave.json'),'r') as cred:
        need = json.load(cred)
    access_token = need['client_id']+':'+need['access_token']
    run_process_symbol_data(access_token)


if __name__ == '__main__':
    timeIn = refresIt()
    if timeIn > 1000:
        pin = getpass("your pin : ")
        refresh.new_access_token(pin)

    main()

