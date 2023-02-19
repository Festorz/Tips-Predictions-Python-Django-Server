from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import (BetikaSubscribers, BetpawaSubscribers, BongobongoSubscribers, FixedMatchesSubscribers, GuruSubscribers, MozzartSubscribers,
 Multibets1x2, MultibetsGG, MultibetsHFT, MultibetsOU, PremiumSubscribers, SportpesaSubscribers, SportybetSubscribers, 
 VIPSubscribers)

from .serializers import (BetikaSerializer, BetpawaSerializer, BongoBongoSerializer, FixedMatchesSerializer, GGMultiSerializer, GuruSerializer, HFTMultiSerializer, IX2MultiSerializer, MozzartSerializer, OVUMultiSerializer, PremiumSerializer, 
SportpesaSerializer, SportybetSerializer, VIPSerializer)

# Create your views here.
    
def subscriber(user, model, serializers):
        subscribe = model.objects.filter(user=user).order_by('-pk')[:1]

        if subscribe.exists():
            sub = subscribe[0]
            expiry = sub.exp
            time = timezone.now()
            print('time is ', time)
            print('exp is ', expiry)
            if time > expiry:
                print('deleted')
                sub.delete()
            serializer = serializers(subscribe, many=True)

        return serializer

@api_view(['POST'])
def vipSubscriber(request):
    try:
        user = request.data['user']
        serializer = subscriber(user, VIPSubscribers, VIPSerializer)

        return Response(serializer.data)
    except:
        return Response({'Error':"Please Subscribe"})

@api_view(['POST'])
def fixedMSubscriber(request):
    try:
        user = request.data['user']
        serializer = subscriber(user, FixedMatchesSubscribers, FixedMatchesSerializer)

        return Response(serializer.data)
    except:
        return Response({'Error':"Please Subscribe"})

@api_view(['POST'])
def premiumSubscriber(request):
    try:
        user = request.data['user']
        serializer = subscriber(user, PremiumSubscribers, PremiumSerializer)

        return Response(serializer.data)
    except:
        return Response({'Error':"Please Subscribe"})


@api_view(['POST'])
def guruSubscriber(request):
    try:
        user = request.data['user']
        serializer = subscriber(user, GuruSubscribers, GuruSerializer)

        return Response(serializer.data)
    except:
        return Response({'Error':"Please Subscribe"})


@api_view(['POST'])
def multi1X2(request):
    try:
        user = request.data['user']
        serializer = subscriber(user, Multibets1x2, IX2MultiSerializer)

        return Response(serializer.data)
    except:
        return Response({'Error':"Please Subscribe"})


@api_view(['POST'])
def multiOvund(request):
    try:
        user = request.data['user']
        serializer = subscriber(user, MultibetsOU, OVUMultiSerializer)

        return Response(serializer.data)
    except:
        return Response({'Error':"Please Subscribe"})


@api_view(['POST'])
def multiGG(request):
    try:
        user = request.data['user']
        serializer = subscriber(user, MultibetsGG, GGMultiSerializer)

        return Response(serializer.data)
    except:
        return Response({'Error':"Please Subscribe"})


@api_view(['POST'])
def multiHft(request):
    try:
        user = request.data['user']
        serializer = subscriber(user, MultibetsHFT, HFTMultiSerializer)

        return Response(serializer.data)
    except:
        return Response({'Error':"Please Subscribe"})

@api_view(['POST'])
def sportpesaSubscriber(request):
    try:
        user = request.data['user']
        # print(user)
        serializer = subscriber(user, SportpesaSubscribers, SportpesaSerializer)

        return Response(serializer.data)
    except:
        return Response({'Error':"Please Subscribe"})


@api_view(['POST'])
def sportybetSubscriber(request):
    try:
        user = request.data['user']
        serializer = subscriber(user, SportybetSubscribers, SportybetSerializer)
        return Response(serializer.data)
    except:
        return Response({'Error':"Please subscribe"})


@api_view(['POST'])
def betikaSubscriber(request):
    try:
        user = request.data['user']
        serializer = subscriber(user, BetikaSubscribers, BetikaSerializer)

        return Response(serializer.data)
    except:
        return Response({'Error':"Please Subscribe"})


@api_view(['POST'])
def betpawaSubscriber(request):
    try:
        user = request.data['user']
        serializer = subscriber(user, BetpawaSubscribers, BetpawaSerializer)

        return Response(serializer.data)
    except:
        return Response({'Error':"Please Subscribe"})


@api_view(['POST'])
def bongobongobetSubscriber(request):
    try:
        user = request.data['user']
        serializer = subscriber(user, BongobongoSubscribers, BongoBongoSerializer)

        return Response(serializer.data)
    except:
        return Response({'Error':"Please Subscribe"})


@api_view(['POST'])
def mozzartSubscriber(request):
    try:
        user = request.data['user']
        serializer = subscriber(user, MozzartSubscribers, MozzartSerializer)

        return Response(serializer.data)
    except:
        return Response({'Error':"Please Subscribe"})

