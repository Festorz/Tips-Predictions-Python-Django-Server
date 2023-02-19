from email.mime import image
from rest_framework import serializers
from .models import (FreeTips, LNMOnline, Jackpots, MultiBetGames,PaypalRecord, PopularGames, Prediction, Results)
from django.contrib.auth import get_user_model


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields =(
            'username', 'first_name','last_name','phone','email','country','password'
        )


class LogInSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields =(
            'username','first_name','phone','email','country','password'
        )


class FreeGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeTips
        fields = (
            'title',
            'games',
            'category'
        )

class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields =(
            'title',
            'games'
        )


class PredictionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields =(
            'title','games',
        )

class PopularSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField('get_image_url')

   
    class Meta:
        model = PopularGames
        fields ='games','images','slug'

    def get_image_url(self, obj):
        request = self.context.get('request')
        home_logo= request.build_absolute_uri(obj.home_logo.url)
        away_logo= request.build_absolute_uri(obj.away_logo.url)
        image= request.build_absolute_uri(obj.image.url)
        data = {"home":home_logo, "away":away_logo, "image":image}
        return data


class JackpotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jackpots
        fields =(
            'games',
        )


class PayPalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaypalRecord
        fields =(
            'user', 'amount','product'
        )
    
class MultibetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultiBetGames
        fields =(
            'category','games',
        )

class LNMOnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = LNMOnline
        fields = ('user', 'PhoneNumber', 'Amount', 'ResultCode','TransactionDate')
