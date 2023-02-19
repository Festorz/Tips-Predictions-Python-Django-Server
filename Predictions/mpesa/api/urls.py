from django.contrib import admin
from django.urls import path
from Predictions.mpesa.api.views import lNMCallbackUrlAPIView

app_name = 'mpesa'
urlpatterns = [
    path('lnm/', lNMCallbackUrlAPIView, name='lnm-callbackurl'),
]
