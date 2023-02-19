from email.mime import image
from django.urls.conf import path
from knox.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

from .views import (freetips, jackpots, login,lNMCallbackUrlAPIView, mpesaPay, multibets, paypalPay, popular, register, reset_password, results, singlePopular, upcomingVip, vip)


app_name = 'tips'

urlpatterns = [
    path('api/', freetips),
    path('register/', register),
    path('login/', login),
    path('resetPassword/', reset_password),
    path('logout/', LogoutView.as_view()),
    path('paypalPay/', paypalPay),
    path('mpesaPay/', mpesaPay),
    path('jackpots/', jackpots),
    path('vip/', vip),
    path('upvip/', upcomingVip),
    path('multibets/', multibets),
    path('results/', results),
    path('popular/', popular),
    path('singleMatch/', singlePopular),
    path('lnm/', lNMCallbackUrlAPIView, name='lnm-callbackurl'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
