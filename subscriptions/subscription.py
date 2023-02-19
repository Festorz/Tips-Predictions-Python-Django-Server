from .models import (BetpawaSubscribers, BongobongoSubscribers, FixedMatchesSubscribers, GuruSubscribers, MozzartSubscribers, Multibets1x2, MultibetsGG, MultibetsHFT, MultibetsOU, PremiumSubscribers,
 SportpesaSubscribers, BetikaSubscribers, SportybetSubscribers, VIPSubscribers)

def update_user(user, product):
    if product == 'sportpesa':
        subscription = SportpesaSubscribers()
        subscription.user = user
        subscription.sportpesa=True
        subscription.save()

    elif product == 'premium':
        subscription = PremiumSubscribers()
        subscription.user = user
        subscription.premium=True
        subscription.save()

    elif product == 'VIP':
        subscription = VIPSubscribers()
        subscription.user = user
        subscription.vip=True
        subscription.save()

    elif product == 'fixedm':
        subscription = FixedMatchesSubscribers()
        subscription.user = user
        subscription.fixed_matches=True
        subscription.save()

    elif product == 'betika':
        subscription = BetikaSubscribers()
        subscription.user = user
        subscription.betika_grand=True
        subscription.save()
        
    elif product == 'betika':
        subscription = BetikaSubscribers()
        subscription.user = user
        subscription.betika_grand=True
        subscription.save()

    elif product == 'betpawa':
        subscription = BetpawaSubscribers()
        subscription.user = user
        subscription.betpawa=True
        subscription.save()

    elif product == 'bongobongo':
        subscription = BongobongoSubscribers()
        subscription.user = user
        subscription.bongobongo=True
        subscription.save()

    elif product == 'mozzart':
        subscription = MozzartSubscribers()
        subscription.user = user
        subscription.mozzart=True
        subscription.save()

    elif product == 'sportybet':
        subscription = SportybetSubscribers()
        subscription.user = user
        subscription.sportybet=True
        subscription.save()

    elif product == '1X2':
        subscription = Multibets1x2()
        subscription.user = user
        subscription.Ix2=True
        subscription.save()

    elif product == 'GG':
        subscription = MultibetsGG()
        subscription.user = user
        subscription.gg=True
        subscription.save()

    elif product == 'OV':
        subscription = MultibetsOU()
        subscription.user = user
        subscription.ovund=True
        subscription.save()

    elif product == 'HTFT':
        subscription = MultibetsHFT()
        subscription.user = user
        subscription.htft=True
        subscription.save()

    elif product == 'guru':
        subscription = GuruSubscribers()
        subscription.user = user
        subscription.guru=True
        subscription.save()

    return product