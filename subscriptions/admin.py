from django.contrib import admin

from .models import (BetikaSubscribers, BetpawaSubscribers, BongobongoSubscribers, FixedMatchesSubscribers, GuruSubscribers
, MozzartSubscribers, Multibets1x2, MultibetsGG, MultibetsHFT, MultibetsOU, PremiumSubscribers, SportpesaSubscribers, SportybetSubscribers, VIPSubscribers)

# Register your models here.
class SubscribersAdmin(admin.ModelAdmin):
    list_display = ['user', 'created','exp']

admin.site.register(VIPSubscribers, SubscribersAdmin)
admin.site.register(FixedMatchesSubscribers, SubscribersAdmin)
admin.site.register(PremiumSubscribers, SubscribersAdmin)
admin.site.register(SportpesaSubscribers, SubscribersAdmin)
admin.site.register(SportybetSubscribers, SubscribersAdmin)
admin.site.register(BetikaSubscribers, SubscribersAdmin)
admin.site.register(BetpawaSubscribers, SubscribersAdmin)
admin.site.register(BongobongoSubscribers, SubscribersAdmin)
admin.site.register(MozzartSubscribers, SubscribersAdmin)
admin.site.register(Multibets1x2, SubscribersAdmin)
admin.site.register(MultibetsOU, SubscribersAdmin)
admin.site.register(MultibetsGG, SubscribersAdmin)
admin.site.register(MultibetsHFT, SubscribersAdmin)
admin.site.register(GuruSubscribers, SubscribersAdmin)
