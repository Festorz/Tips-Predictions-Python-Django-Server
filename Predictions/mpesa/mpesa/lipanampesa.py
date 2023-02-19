import requests

from Predictions.models import User
from .access_token import generate_access_token
from .encode import generate_password
from .utils import get_timestamp
from .import keys

formatted_time = get_timestamp()

decoded_password = generate_password(formatted_time)


def lipa_na_mpesa(phone, amount, user):
    access_token = generate_access_token()
    # api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest" #test
    api_url = "https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest" #live
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": keys.business_shortcode,
        "Password": decoded_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerBuyGoodsOnline",
        "Amount": amount,
        "PartyA": phone,
        "PartyB": keys.shortcode,
        "PhoneNumber": phone,
        "CallBackURL": "https://tips-predictions.com/payments/lnm/",
        "AccountReference": "9443897",
        "TransactionDesc": "Pay today"
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)
    print(user)
    subscriber =  User.objects.get(username=user)

    # user.transactionID=''
    # user.save()
    print("Running lipa ")


# lipa_na_mpesa()
