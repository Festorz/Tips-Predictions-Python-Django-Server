from django.urls.conf import path
from .views import (
    betikaSubscriber, betpawaSubscriber, bongobongobetSubscriber, fixedMSubscriber, guruSubscriber, mozzartSubscriber, multi1X2, multiGG, multiHft, multiOvund, premiumSubscriber, 
    sportpesaSubscriber, sportybetSubscriber, vipSubscriber)

app_name = 'subs'

urlpatterns = [
    path('premium/', premiumSubscriber),
    path('vip/', vipSubscriber),
    path('fixedm/', fixedMSubscriber),
    path('guru/', guruSubscriber),
    path('sportpesa/', sportpesaSubscriber),
    path('sportybet/', sportybetSubscriber),
    path('betika/', betikaSubscriber),
    path('betpawa/', betpawaSubscriber),
    path('bongobongo/', bongobongobetSubscriber),
    path('mozzart/', mozzartSubscriber),
    path('1x2/', multi1X2),
    path('gg/', multiGG),
    path('ovund/', multiOvund),
    path('htft/', multiHft),
]