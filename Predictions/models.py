from datetime import datetime
import json
from pyexpat import model
from django.contrib.postgres import fields
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils.text import slugify

from django.dispatch import receiver
from django.urls import reverse
from django.core.mail import send_mail  
from django_rest_passwordreset.signals import reset_password_token_created




jackpots_category = (
    ('MG', 'Sportpesa Mega'),
    ('SP', 'Sportpesa weekly'),
    ('BG', 'Betika Grand'),
    ('BTX', 'Betpawa 1X2'),
    ('MZ', 'Mozzart'),
    ('BN', 'Bongobongo'),
    ('SPT', 'SportyBet'),
    ('BM', 'Betika Midweek'),
)

record_category = (
    ('MT', 'Matches'),
    ('RS', 'Match Results'),

)

prediction_level = (
    ('PR', 'Premium'),
    ('FM', 'Fixed Matches'),
    ('UFM', 'Upcoming Fixed Matches'),
    ('VIP', 'VIP'),
    ('UVIP', 'Upcoming VIP'),

)
multibets = (
    ('12', '1X2'),
    ('GG', 'GG'),
    ('OU', 'Over Under'),
    ('HF', 'Half/Full Time')
)

tips_category = (
    ('GR', 'Guru Tips'),
    ('FR', 'Free Tips')
)


# Create your models here.
 
class OldJSonField(fields.JSONField):
    def db_type(self, connection):
        return 'json'

class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, email, phone, country, password):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, phone=phone, country=country, first_name=first_name,
                          last_name=last_name)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, phone, password, country=None, first_name=None, last_name=None):
        user = self.create_user(username=username, email=email, phone=phone, password=password, country=country,
                                first_name=first_name, last_name=last_name)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(max_length=32, unique=True, )
    email = models.EmailField(max_length=32)
    phone = models.CharField(max_length=13, blank=False)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    transactionID = models.CharField(max_length=100, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    country = models.CharField(max_length=200, null=True, blank=True)


    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    REQUIRED_FIELDS = ["email", "phone"]
    USERNAME_FIELD = "username"
    objects = UserManager()

    def __str__(self):
        return self.username

  
    class Meta:
        ordering = ['-date_added']



# resetting Password
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), 
    reset_password_token.key)
    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "bettcare@gmail.com",
        # to:
        [reset_password_token.email]
    )

class FreeTips(models.Model):
    title = models.CharField(max_length=50, default='')
    tips_file = models.FileField(upload_to='games')
    category = models.CharField(
        choices=tips_category, max_length=2, default='')
    games = models.JSONField(editable=False)
    date = models.DateTimeField(blank=True, null=True)
    odds = models.FloatField(default=1)
    yesterday_odd = models.FloatField(default=1)
    winning_rate = models.PositiveIntegerField(default=90)


    def win_rate(self):
        rt = 0
        if self.winning_rate >= 90:
            rt = 80
        else:
            rt = 90
        return rt

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.games = json.load(self.tips_file)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Free Tips'


class MultiBetGames(models.Model):
    title = models.CharField(max_length=50, default='')
    games_file = models.FileField(upload_to='multi bets', blank=True, null=True)
    games = models.JSONField(editable=False, null=True, blank=True)
    # games = OldJSonField(editable=False, null=True, blank=True)
    category = models.CharField(
        choices=multibets, max_length=3)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Multi Bet Games'

    def save(self, *args, **kwargs):
        self.games = json.load(self.games_file)
        super().save(*args, **kwargs)

class Prediction(models.Model):
    title = models.CharField(max_length=50, default='')
    games_file = models.FileField(upload_to='games')
    games = models.JSONField(editable=False)
    category = models.CharField(
        choices=prediction_level, max_length=5)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.games = json.load(self.games_file)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Predictions'

        
class PopularGames(models.Model):
    title = models.CharField(max_length=50, default='')
    games_file = models.FileField(upload_to='popular')
    games = OldJSonField(editable=False)
    home_logo = models.ImageField(upload_to='popular-images', default='')
    away_logo = models.ImageField(upload_to='popular-images', default='')
    image = models.ImageField(upload_to='popular-images', default='', blank=True, null=True)
    slug = models.SlugField(default='', null=False, editable=False)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.games = json.load(self.games_file)
        self.slug = slugify(self.title, allow_unicode=True,)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Popular Games'
        

class Jackpots(models.Model):
    title = models.CharField(max_length=80, default='')
    jackpot_file = models.FileField(upload_to='jackpots')
    games = models.JSONField(editable=False,)
    category = models.CharField(choices=jackpots_category, max_length=3)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Jackpots'

    def save(self, *args, **kwargs):
        self.games = json.load(self.jackpot_file)
        super().save(*args, **kwargs)


# subscribers manenons



class LNMOnline(models.Model):
    user = models.CharField(default='', max_length=254)
    CheckoutRequestID = models.CharField(max_length=50)
    MerchantRequestID = models.CharField(max_length=20)
    ResultCode = models.IntegerField()
    ResultDesc = models.CharField(max_length=120)
    Amount = models.FloatField()
    MpesaReceiptNumber = models.CharField(max_length=20)
    Balance = models.CharField(max_length=12)
    TransactionDate = models.DateTimeField()
    PhoneNumber = models.CharField(max_length=13)

    def __str__(self):
        return self.user


class PaypalRecord(models.Model):
    user = models.CharField(max_length=254, default='')
    amount = models.CharField(default='', max_length=20)
    product = models.CharField(default='', max_length=100)

    class Meta:
        verbose_name_plural = 'PayPal Records'
    
    def __str__(self):
        return self.user

class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contact Us'
        ordering = ['-date_added']


class Results(models.Model):
    title = models.CharField(max_length=50, default='')
    results = models.FileField(upload_to='results')
    games = models.JSONField(editable=False)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Results'


    def save(self, *args, **kwargs):
        self.games = json.load(self.results)
        super().save(*args, **kwargs)

