from .fyers_call import Authentication
from colorama import Fore
import os
import json



def gen():
    client_id = input("app_id: ")
    secret_key = input("secret_key: ")
    secrets = Authentication.step(client_id,secret_key)
    if secrets['s'] == 'error':
        print(secrets)
        exit(Fore.RED + f"\n **********************************{secrets['message']}************************")
        
    secrets["client_id"] = client_id

    secrets["secret_key"] = secret_key
    print(secrets)

    with open(os.path.join(os.getcwd(),'helper/fyers_call/fyerSave.json'),"w") as saves:
        json.dump(secrets,saves)
    
    print(Fore.GREEN + "**************************Credentials Generated*********************************")
