import os
import json
from .hash import hash_of
import requests
from colorama import Fore 


def new_access_token(pin):
    with open(os.path.join(os.getcwd(),'helper/fyers_call/fyerSave.json'),'r') as saves:
        needed = json.load(saves)
    try:    
        if 'refresh_token' in needed:
            appIdHash = hash_of(needed['client_id']+needed['secret_key'])
    except Exception as err:
        exit(Fore.RED +f'{err} ')
            
    url = 'https://api.fyers.in/api/v2/validate-refresh-token'
    headers = {
    'Content-Type': 'application/json'
    }
    data = {
    'grant_type': 'refresh_token',
    'appIdHash': appIdHash,
    'refresh_token': needed['refresh_token'],
    'pin': pin
    }
    response = requests.post(url,headers=headers,json=data)
    if response.status_code == 200:
        response = response.json()
        needed['access_token'] = response['access_token']
        with open(os.path.join(os.getcwd(),'helper/fyers_call/fyerSave.json'),'w') as saves:
            json.dump(needed,saves)
    else:
        exit(Fore.RED + 'use --gen option unable to refresh')