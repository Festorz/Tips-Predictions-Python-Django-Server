import requests
from requests.auth import HTTPBasicAuth
from .import keys


def generate_access_token():
    consumer_key = keys.consumer_key
    consumer_secret = keys.consumer_secret
    # api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials" #test
    # api_URL="https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    api_URL = "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials" #live
    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))

    # print('this is r',r)
    print(r.json())

    # {'access_token': 'kBurxhjaTs0iEhwsqKH1lXThsHmE', 'expires_in': '3599'}
    json_response = r.json()

    my_access_token = json_response['access_token']

    return my_access_token

# generate_access_token()
