import requests
from . import keys
from .access_token import generate_access_token


def register_url():
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"

    headers = {"Authorization": "Bearer %s" % access_token}

    request = {"ShortCode": keys.shortcode,
               "ResponseType": "Completed",
               "ConfirmationURL": "https://fierce-castle-84478.herokuapp.com/api/payments/c2b-confirmation/",
               "ValidationURL": "https://fierce-castle-84478.herokuapp.com/api/payments/c2b-validation/",
               }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)


# register_url()

def simulate_c2b_transactions():
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {"ShortCode": keys.shortcode,
               "CommandID": "CustomerPayBillOnline",
               "Amount": "1",
               "Msisdn": keys.test_msisdn,
               "BillRefNumber": "12345678"}

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)


simulate_c2b_transactions()
