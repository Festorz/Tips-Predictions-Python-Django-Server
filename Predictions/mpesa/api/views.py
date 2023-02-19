from datetime import datetime

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from Predictions.mpesa.api.serializers import LNMOnlineSerializer
from Predictions.models import LNMOnline, User
from rest_framework.response import Response
import pytz
from subscriptions.subscription import update_user
from rest_framework.decorators import api_view
from Predictions.emails import mpesaSubscriptionsEmail

from  django.core.cache import cache
from django.utils.timezone import localtime



@api_view(['POST'])
def lNMCallbackUrlAPIView(request):
    print(request.data, 'this is request.data')
     
    result_code = request.data['Body']['stkCallback']['ResultCode']
    result_description = request.data['Body']['stkCallback']['ResultDesc']

    if result_code == 0:
        merchant_request_id = request.data['Body']['stkCallback']['MerchantRequestID']
        checkout_request_id = request.data['Body']['stkCallback']['CheckoutRequestID']
        # result_code = 0
        amount = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value']
        mpesa_receipt_number = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value']
        balance = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][2]['Value']
        transaction_date = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][3]['Value']
        phone_number = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value']

        str_transaction_date = str(transaction_date)

        transaction_datetime = datetime.strptime(
            str_transaction_date, "%Y%m%d%H%M%S")

        # aware_transaction_datetime = pytz.utc.localize(transaction_datetime)
        aware_transaction_datetime = localtime(transaction_datetime)

        
        user = cache.get('user', 'has expired')
        product = cache.get('product', 'has expired')
        email = cache.get('email', 'has expired')
        
        
        cache.set('result_code', result_code, 30)

   
        payment = LNMOnline()
        payment.user = user
        payment.CheckoutRequestID=checkout_request_id
        payment.MerchantRequestID=merchant_request_id
        payment.ResultCode = result_code
        payment.ResultDesc=result_description
        payment.Amount=amount
        payment.MpesaReceiptNumber=mpesa_receipt_number
        payment.Balance=balance
        payment.TransactionDate=aware_transaction_datetime
        payment.PhoneNumber=phone_number

        payment.save()

        update_user(user, product)
        mpesaSubscriptionsEmail(request, user, email, product, amount)
        

    return Response(
        {'Result code':result_code, 'result_description':result_description}
    )



# class LNMCallbackUrlAPIView(CreateAPIView):
#     queryset = LNMOnline.objects.all()
#     serializer_class = LNMOnlineSerializer
#     permission_classes = [AllowAny]

#     def create(self, request):
#         print(request.data, 'this is request.data')

#         merchant_request_id = request.data['Body']['stkCallback']['MerchantRequestID']
#         checkout_request_id = request.data['Body']['stkCallback']['CheckoutRequestID']
#         result_code = request.data['Body']['stkCallback']['ResultCode']
#         result_description = request.data['Body']['stkCallback']['ResultDesc']
#         amount = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][0]['value']
#         mpesa_receipt_number = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][1]['value']
#         balance = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][2]['value']
#         transaction_date = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][3]['value']
#         phone_number = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][4]['value']

#         str_transaction_date = str(transaction_date)

#         transaction_datetime = datetime.strptime(
#             str_transaction_date, "%Y5m%d%H%M%S")

#         aware_transaction_datetime = pytz.utc.localize(transaction_datetime)

#         user = request.session['user']
#         product = request.session['product']

#         if result_code == 0:
#             payment = LNMOnline()
#             payment.user = user
#             payment.CheckoutRequestID=checkout_request_id
#             payment.MerchantRequestID=merchant_request_id
#             payment.ResultCode = result_code
#             payment.ResultDesc=result_description
#             payment.Amount=amount,
#             payment.MpesaReceiptNumber=mpesa_receipt_number
#             payment.Balance=balance
#             payment.TransactionDate=aware_transaction_datetime
#             payment.PhoneNumber=phone_number

#             payment.save()

#             update_user(user, product)

#         return Response(
#             {'Result code':result_code, 'result_description':result_description}
#         )
