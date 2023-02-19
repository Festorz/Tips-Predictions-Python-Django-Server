from datetime import datetime
import re
from unicodedata import category
from urllib import response
from django.urls import reverse
import pytz

from blog.models import Post
from django.contrib.auth.hashers import check_password, make_password
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from knox.models import AuthToken
from requests.exceptions import ConnectionError
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from subscriptions.subscription import update_user
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail

from Predictions.mpesa.mpesa.lipanampesa import lipa_na_mpesa

from .emails import mpesaSubscriptionsEmail, paypalSubscriptionsEmail,signIn
from .models import (ContactUs, FreeTips, Jackpots, LNMOnline, MultiBetGames, PopularGames,
                     Prediction, Results, User)
from .serializers import (FreeGuruSerializer, JackpotsSerializer, LNMOnlineSerializer,
                          LogInSerializer, MultibetsSerializer, PayPalSerializer, PopularSerializer, PredictionsSerializer,
                          RegisterSerializer, ResultsSerializer)

from  django.core.cache import cache


# Create your views here.

    
@api_view(['POST'])
def register(request):
    username = request.data['username']
    email = request.data['email']
    if User.objects.filter(username=username).exists():
        return Response({'Error':"Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif User.objects.filter(email=email).exists():
        return Response({'Error':"Email already exists"}, status=status.HTTP_400_BAD_REQUEST)
    
    

    password = request.data['password']
    request.data['password'] = make_password(password)
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        token = AuthToken.objects.create(user)
        mToken = AuthToken.objects.filter(user=user).order_by('-pk')[:1]
        signIn(request)

        if mToken.exists():
            date = mToken[0].expiry


    return Response({
        "user":serializer.data,
         "token":token[1],
         'exp':date
        })

  
@api_view(['POST'])
def login(request):
    email = request.data['email']
    password = request.data['password']
    try:
        user = User.objects.get(email=email)
        serializer = LogInSerializer(user, many=False)

        if check_password(password,user.password):
            token = AuthToken.objects.create(user)
            print(token)
            mToken = AuthToken.objects.filter(user=user).order_by('-pk')[:1]
            if mToken.exists():
                date = mToken[0].expiry
                
            return Response({
                "user":serializer.data,
                "token":token[1],
                'exp':date
                })
        else:
            return Response({'Error':"Invalid Credentials"}, status=status.HTTP_404_NOT_FOUND)
    except ObjectDoesNotExist:
        return Response({'Error':"User with that email does not exist"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def reset_password(request):
    email = request.data['email']
    # username = request.data['username']
    password = request.data['password']
    try:
        newpass = make_password(password)
        user = User.objects.get(email=email)
        user.password = newpass
        user.save()
        return Response({'message':'Password Reset was successful'})
    except ObjectDoesNotExist:
        return Response({'Error':"User with that email does not exist"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def freetips(request):
    cat = request.data['category']
    games = FreeTips.objects.filter(category=cat).order_by('-pk')[:1]
    serializer = FreeGuruSerializer(games, many=True).data
    return Response(serializer)


@api_view(['GET'])
def results(request):
    permission_classes = [
        permissions.IsAuthenticated,
        ]

    results = Results.objects.all().order_by('-pk')[:6]
    serializer = ResultsSerializer(results, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def popular(request):
    popular = PopularGames.objects.all().order_by('-pk')[:6]
    serializer = PopularSerializer(popular, many=True, context={"request": 
                      request})
    return Response(serializer.data)


@api_view(['POST'])
def singlePopular(request):
    slug = request.data['id']
    games = PopularGames.objects.filter(slug=slug).order_by('-pk')[:1]
    serializer = PopularSerializer(games, many=True, context={"request": 
                      request})
    return Response(serializer.data)


@api_view(['POST'])
def jackpots(request):
    category = request.data['category']

    games = Jackpots.objects.filter(category=category).order_by('-pk')[:1]
    serializer = JackpotsSerializer(games, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def multibets(request):
    category = request.data['category']

    games = MultiBetGames.objects.filter(category=category).order_by('-pk')[:1]
    serializer = MultibetsSerializer(games, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def vip(request):
    category = request.data['category']

    games = Prediction.objects.filter(category=category).order_by('-pk')[:1]
    serializer = PredictionsSerializer(games, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def upcomingVip(request):
    category = request.data['category']

    games = Prediction.objects.filter(category=category)
    serializer = PredictionsSerializer(games, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def paypalPay(request):
    print(request.data)
    try:
        data = request.data['paymentdata']
        user = data['user']
        product = data['product']
        update_user(user, product)
        paypalSubscriptionsEmail(request)
        serializer = PayPalSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            
        return Response(serializer.data)
    
    except:
        return Response({'Error':'Cannot process data'})
  

@api_view(['POST'])
def mpesaPay(request):
    print(request.data)
    try:
        data = request.data
        user = data['paymentdata']['user']
        phone = data['paymentdata']['phone_number']
        print(phone)
        amount = data['paymentdata']['amount']
        product = data['paymentdata']['product']
        email = data['paymentdata']['email']

        cache.set('user', user, 60)
        cache.set('product', product, 60)
        cache.set('email', email, 60)
        
        lipa_na_mpesa(phone, amount, user)
        # mpesaSubscriptionsEmail(request, user, email, product,amount)
        # result = request.session['response']
        
        response = 'Processing your subscription....'
        return Response({'response':response})

    except ConnectionError as e: 
        return Response({'Error':'Error.. No Internet Connection'}, status=status.HTTP_404_NOT_FOUND)
  
@api_view(['POST'])
def lNMCallbackUrlAPIView(request):
    print(request.data, 'this is request.data')

    # merchant_request_id = request.data['Body']['stkCallback']['MerchantRequestID']
    # checkout_request_id = request.data['Body']['stkCallback']['CheckoutRequestID']
    # result_code = request.data['Body']['stkCallback']['ResultCode']
    result_code = 0
    # result_description = request.data['Body']['stkCallback']['ResultDesc']
    # amount = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][0]['value']
    # mpesa_receipt_number = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][1]['value']
    # balance = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][2]['value']
    # transaction_date = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][3]['value']
    # phone_number = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][4]['value']

    # str_transaction_date = str(transaction_date)

    # transaction_datetime = datetime.strptime(
    #     str_transaction_date, "%Y5m%d%H%M%S")

    # aware_transaction_datetime = pytz.utc.localize(transaction_datetime)

    # user = request.session['user']
    # product = request.session['product']

    if result_code == 0:
        payment = LNMOnline()
        payment.user = "user"
        payment.CheckoutRequestID="checkout_request_id"
        payment.MerchantRequestID="merchant_request_id"
        payment.ResultCode = result_code
        payment.ResultDesc="result_description"
        payment.Amount=1
        payment.MpesaReceiptNumber="mpesa_receipt_number"
        payment.Balance="balance"
        # payment.TransactionDate="aware_transaction_datetime"
        payment.PhoneNumber="phone_number"

        payment.save()

        # update_user(user, product)

    return Response(
        {'Result code':result_code, 'result_description':"result_description"}
    )
