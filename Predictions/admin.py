from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import (FreeTips, PopularGames, Prediction, User, ContactUs,
                     MultiBetGames, Results, Jackpots, PaypalRecord, LNMOnline)


# Register your models here.


class FreeTipsAdmin(admin.ModelAdmin):
    list_display = ['title', 'tips_file', 'category']



class JackpotsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']




class MultibetGamesAdmin(admin.ModelAdmin):
    list_display = ['title','games_file','games', 'category']


class ResultsAdmin(admin.ModelAdmin):
    list_display = ['title', 'results']


class PredictionAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'games_file']

    list_filter = [
        'title',
        'category',
    ]

class PopularAdmin(admin.ModelAdmin):
    list_display = ['title','games_file','slug']


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'date_added', 'phone', 'country' ]

    list_display_links = [
        'username',

    ]

    search_fields = ['username', 'first_name', 'last_name']

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False


class ContactAdmin(admin.ModelAdmin):
    list_display = ['date_added', 'name', 'email', 'subject', 'message']

class PaypalAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'product']

class MpesaAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'product']


class MultibetsAdmin(admin.ModelAdmin):
    list_display = ['date', 'user', 'booked',
                    'btts', 'ov_und', 'iX2', 'ht_ft']

    list_filter = [
        'booked', 'btts', 'ov_und', 'iX2', 'ht_ft',
    ]

    search_fields = ['name', ]



admin.site.register(User, UserAdmin)
admin.site.register(FreeTips, FreeTipsAdmin)
admin.site.register(Prediction, PredictionAdmin)
admin.site.register(PopularGames, PopularAdmin)
admin.site.register(ContactUs, ContactAdmin)
# admin.site.register(MultiBetCustomers, MultibetsAdmin)
admin.site.register(MultiBetGames, MultibetGamesAdmin)
admin.site.register(Results, ResultsAdmin)
admin.site.register(Jackpots, JackpotsAdmin)
admin.site.register(PaypalRecord, PaypalAdmin)
admin.site.register(LNMOnline)

