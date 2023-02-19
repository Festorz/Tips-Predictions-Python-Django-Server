from Predictions.models import LNMOnline
from rest_framework import serializers


class LNMOnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = LNMOnline
        fields = ('user', 'PhoneNumber', 'Amount', 'ResultCode','TransactionDate')
