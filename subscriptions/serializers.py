from rest_framework import serializers
from .models import (BetikaSubscribers, BetpawaSubscribers, BongobongoSubscribers, FixedMatchesSubscribers, GuruSubscribers, MozzartSubscribers, Multibets1x2, MultibetsGG, MultibetsHFT, MultibetsOU, PremiumSubscribers, SportpesaSubscribers, SportybetSubscribers, VIPSubscribers)


class FixedMatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedMatchesSubscribers
        fields =(
            'user', 'fixed_matches',
        )
    
class VIPSerializer(serializers.ModelSerializer):
    class Meta:
        model = VIPSubscribers
        fields =(
            'user', 'vip',
        )
    
class PremiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumSubscribers
        fields =(
            'user', 'premium',
        )

class GuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuruSubscribers
        fields =(
            'user', 'guru',
        )

class IX2MultiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multibets1x2
        fields =(
            'user', 'Ix2',
        )
        
class GGMultiSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultibetsGG
        fields =(
            'user', 'gg',
        )
class OVUMultiSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultibetsOU
        fields =(
            'user', 'ovund',
        )

class HFTMultiSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultibetsHFT
        fields =(
            'user', 'htft',
        )
    
class SportpesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportpesaSubscribers
        fields =(
            'user', 'sport_mega',
        )
    
class BetikaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BetikaSubscribers
        fields =(
            'user', 'betika_grand',
        )
    
class SportybetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportybetSubscribers
        fields =(
            'user', 'sportybet','exp','created'
        )
    
class BetpawaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BetpawaSubscribers
        fields =(
            'user', 'betpawa',
        )
    
class BongoBongoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BongobongoSubscribers
        fields =(
            'user', 'bongobongo',
        )
    
class MozzartSerializer(serializers.ModelSerializer):
    class Meta:
        model = MozzartSubscribers
        fields =(
            'user', 'mozzart',
        )
