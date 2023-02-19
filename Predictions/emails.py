from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
from urllib.parse import quote
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string


# paypal email
def paypalSubscriptionsEmail(request):
    data = request.data['paymentdata']
    user = data['user']
    product = data['product']
    email = data['email']
    amount = data['amount']
    current_site = get_current_site(request)
    subject = 'New Subscription'
    message = f'''{current_site.domain} 
Hello admin, Good news.. new user subscribed today through paypal
Name : {user},
He purchased: {product},
Amount payed: {amount}
Please ensure they receive tips today in time.
tips-predictions.com,
king of betting tips.'''

    message2 = f'''{current_site.domain} 
Hello {user}, Your subscription for {product} was successful. Please
reload the page to view your tips. Thank you and welcome again our 
dear customer.'''

    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['bettcare@gmail.com','festaskirui@gmail.com' ]
    recipient_list2=[email,]
    datatuple = (
        (subject, message, email_from, recipient_list),
        (subject, message2, email_from, recipient_list2),
    )
    send_mass_mail(datatuple)

# mpesa email
def mpesaSubscriptionsEmail(request, user, email, product, amount):
    current_site = get_current_site(request)
    subject = 'New Subscription'
    message = f'''{current_site.domain} 
Hello admin, Good news.. new user subscribed today through Mpesa
Name : {user},
He purchased: {product},
Amount : {amount}
Please ensure they receive tips today in time.
tips-predictions.com,
king of betting tips.'''

    message2 = f'''{current_site.domain} 
Hello {user}, Your subscription for {product} was successful. Please
reload the page to view your tips. Thank you and welcome again our 
dear customer.'''

    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['bettcare@gmail.com','festaskirui@gmail.com' ]
    recipient_list2=[email,]
    datatuple = (
        (subject, message, email_from, recipient_list),
        (subject, message2, email_from, recipient_list2),
    )
    send_mass_mail(datatuple)


# sign in welcoming email
def signIn(request):
    username = request.data['username']
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    phone = request.data['phone']
    country = request.data['country']
    email = request.data['email']

    message = f'''Hello { username }, welcome to tips-prediction.com, 
the home of sure tips and predictions that guarantee your success in betting. 
Your info is as follows:
First Name is { first_name }

Last name is { last_name }

Mobile number is {phone }

Country is number is {country }

What we offer in tips-prediction.com:
Among the betting markets we have the;
1. fixed matches
2. vip tips
3. premium tips
4. guru tips 
5. multibets
6. Jackpot predictions

Their distinctive pricing is as below:
FIXED MATCHES - $120 or Ksh 10000,
VIP TIPS - $12 or Ksh 1000,
PREMIUM TIPS - $3 or Ksh 300,
GURU TIPS - $1 or Ksh 100,
MULTIBETS - $2 or Ksh 200 
Jackpots - $3 or Ksh 300. 

NOTE:
Once you have paid we will update your credentials and you will be able to view the predictions on our site. 
Kindly note that We don't send any games to you through sms, just refresh the page after 2 mins and you 
will be viewing the football predictions that you subscribed for.

'''

    subject = 'Welcome to tips-predictions.com'
    subject2 = 'New User Registration at tips-predictions.com'
    message2 = f'''
    Hello tips admin,

    You are receiving this email because a new user signed in.
    Please check to confirm.
    User Name: {username}
    First Name: {first_name}

    Last Name: {last_name},

    Email: {email},

    Phone Number: {phone}

    Country: {country}


    Again welcome sir...this site is dope as ever

    '''

    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    recipient_list2 = ["bettcare@gmail.com", "festaskirui@gmail.com"]
    datatuple = (
        (subject, message, email_from, recipient_list),
        (subject2, message2, email_from, recipient_list2)
    )
    send_mass_mail(datatuple,fail_silently=False)
