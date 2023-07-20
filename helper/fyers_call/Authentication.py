from fyers_api import fyersModel
from fyers_api import accessToken
from colorama import Fore



def step(client_id,secret_key):
    
    redirect_uri = "https://google.com"
    response_type = "code"
    state = ""
    grant_type =  "authorization_code"

    session = accessToken.SessionModel(
                                    client_id=client_id,
                                    secret_key=secret_key,redirect_uri=redirect_uri, 
                                    response_type=response_type, grant_type=grant_type
                                    )
    response = session.generate_authcode()
    # response will give link 
    print(Fore.BLUE + response)
    print(Fore.GREEN)
    auth_code = input("auth_code: ")
    session.set_token(auth_code)
    response = session.generate_token()
    return response
