from datetime import datetime, timedelta

from django.db import models
from django.utils import timezone


class VIPSubscribers(models.Model):
    user = models.CharField(default='', max_length=254)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    exp = models.DateTimeField(blank=True, null=True, editable=False)
    vip = models.BooleanField(default=False)
   
    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        expiry = timedelta(hours=36)
        self.exp = timezone.now() + expiry
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'VIP Subscribers'


class FixedMatchesSubscribers(models.Model):
    user = models.CharField(default='', max_length=254)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    exp = models.DateTimeField(blank=True, null=True)
    fixed_matches = models.BooleanField(default=False)
   
    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        expiry = timedelta(days=7)
        self.exp = timezone.now() + expiry
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Fixed Matches Subscribers'

class PremiumSubscribers(models.Model):
    user = models.CharField(default='', max_length=254)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    exp = models.DateTimeField(blank=True, null=True, editable=False)
    premium = models.BooleanField(default=False)
   
    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        expiry = timedelta(hours=16)
        self.exp = timezone.now() + expiry
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Premium Subscribers'

class GuruSubscribers(models.Model):
    user = models.CharField(default='', max_length=254)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    exp = models.DateTimeField(blank=True, null=True, editable=False)
    guru = models.BooleanField(default=False)
   
    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        expiry = timedelta(hours=14)
        self.exp = timezone.now() + expiry
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Guru Subscribers'


class Multibets1x2(models.Model):
    user = models.CharField(default='', max_length=254)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    exp = models.DateTimeField(blank=True, null=True, editable=False)
    Ix2 = models.BooleanField(default=False)
   
    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        expiry = timedelta(hours=14)
        self.exp = timezone.now() + expiry
        super().save(*args, **kwargs)
    

    class Meta:
        verbose_name_plural = 'Multibets 1X2'

class MultibetsHFT(models.Model):
    user = models.CharField(default='', max_length=254)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    exp = models.DateTimeField(blank=True, null=True, editable=False)
    htft = models.BooleanField(default=False)
   
    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        expiry = timedelta(hours=14)
        self.exp = timezone.now() + expiry
        super().save(*args, **kwargs)
    

    class Meta:
        verbose_name_plural = 'Multibets HTFT'

class MultibetsOU(models.Model):
    user = models.CharField(default='', max_length=254)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    exp = models.DateTimeField(blank=True, null=True, editable=False)
    ovund = models.BooleanField(default=False)
   
    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        expiry = timedelta(hours=14)
        self.exp = timezone.now() + expiry
        super().save(*args, **kwargs)
    

    class Meta:
        verbose_name_plural = 'Multibets Over Under'

class MultibetsGG(models.Model):
    user = models.CharField(default='', max_length=254)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    exp = models.DateTimeField(blank=True, null=True, editable=False)
    gg = models.BooleanField(default=False)
   
    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        expiry = timedelta(hours=14)
        self.exp = timezone.now() + expiry
        super().save(*args, **kwargs)
    

    class Meta:
        verbose_name_plural = 'Multibets GG'



class SportpesaSubscribers(models.Model):
    user = models.CharField(default='', max_length=254)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    exp = models.DateTimeField(blank=True, null=True, editable=False)
    sport_mega = models.BooleanField(default=False)
    sportpesa = models.BooleanField(default=False)
   
    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        expiry = timedelta(days=7)
        self.exp = timezone.now() + expiry
        super().save(*args, **kwargs)
    

    class Meta:
        verbose_name_plural = 'Sportpesa Subscribers'

class BetikaSubscribers(models.Model):
    user = models.CharField(default='', max_length=254)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    exp = models.DateTimeField(blank=True, null=True, editable=False)
    betika_grand = models.BooleanField(default=False)
    midweek = models.BooleanField(default=False)
   
    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        expiry = timedelta(days=7)
        self.exp = timezone.now() + expiry
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Betika Subscribers'
    
class BetpawaSubscribers(models.Model):
    user = models.CharField(default='', max_length=254)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    exp = models.DateTimeField(blank=True, null=True, editable=False)    
    betpawa = models.BooleanField(default=False)
   
    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        expiry = timedelta(days=7)
        self.exp = timezone.now() + expiry
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Betpawa Subscribers'
    
class BongobongoSubscribers(models.Model):
    user = models.CharField(default='', max_length=254)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    exp = models.DateTimeField(blank=True, null=True, editable=False)
    bongobongo = models.BooleanField(default=False)
   
    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        expiry = timedelta(days=7)
        self.exp = timezone.now() + expiry
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'BongoBongo Subscribers'
    
class MozzartSubscribers(models.Model):
    user = models.CharField(default='', max_length=254)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    exp = models.DateTimeField(blank=True, null=True, editable=False)
    mozzart = models.BooleanField(default=False)
   
    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        expiry = timedelta(days=7)
        self.exp = timezone.now() + expiry
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Mozzart Subscribers'
    

class SportybetSubscribers(models.Model):
    user = models.CharField(default='', max_length=254)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    exp = models.DateTimeField(blank=True, null=True, editable=False)
    sportybet = models.BooleanField(default=False)
   
    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        expiry = timedelta(days=7)
        self.exp = datetime.now()+expiry
        super().save(*args, **kwargs)
  
    class Meta:
        verbose_name_plural = 'Sportybet Subscribers'
    

