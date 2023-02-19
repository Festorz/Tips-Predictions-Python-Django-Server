# Generated by Django 3.2.5 on 2022-03-09 13:30

import django.contrib.postgres.fields.hstore
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Contact Us',
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='FreeTips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('tips_file', models.FileField(upload_to='games')),
                ('category', models.CharField(choices=[('GR', 'Guru Tips'), ('FR', 'Free Tips')], default='', max_length=2)),
                ('games', models.JSONField(editable=False)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('odds', models.FloatField(default=1)),
                ('yesterday_odd', models.FloatField(default=1)),
                ('winning_rate', models.PositiveIntegerField(default=90)),
            ],
            options={
                'verbose_name_plural': 'Free Tips',
            },
        ),
        migrations.CreateModel(
            name='Jackpots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=80)),
                ('jackpot_file', models.FileField(upload_to='jackpots')),
                ('games', models.JSONField(editable=False)),
                ('category', models.CharField(choices=[('MG', 'Sportpesa Mega'), ('SP', 'Sportpesa weekly'), ('BG', 'Betika Grand'), ('BTX', 'Betpawa 1X2'), ('MZ', 'Mozzart'), ('BG', 'Bongobongo'), ('SPT', 'SportyBet'), ('BM', 'Betika Midweek')], max_length=3)),
            ],
            options={
                'verbose_name_plural': 'Jackpots',
            },
        ),
        migrations.CreateModel(
            name='LNMOnline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=254)),
                ('CheckoutRequestID', models.CharField(max_length=50)),
                ('MerchantRequestID', models.CharField(max_length=20)),
                ('ResultCode', models.IntegerField()),
                ('ResultDesc', models.CharField(max_length=120)),
                ('Amount', models.FloatField()),
                ('MpesaReceiptNumber', models.CharField(max_length=20)),
                ('Balance', models.CharField(max_length=12)),
                ('TransactionDate', models.DateTimeField()),
                ('PhoneNumber', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='MultiBetGames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('games_file', models.FileField(blank=True, null=True, upload_to='multi bets')),
                ('games', django.contrib.postgres.fields.hstore.HStoreField(blank=True, editable=False, null=True)),
                ('category', models.CharField(choices=[('12', '1X2'), ('GG', 'GG'), ('OU', 'Over Under'), ('HF', 'Half/Full Time')], max_length=3)),
            ],
            options={
                'verbose_name_plural': 'Multi Bet Games',
            },
        ),
        migrations.CreateModel(
            name='PaypalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=254)),
                ('amount', models.CharField(default='', max_length=20)),
                ('product', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'PayPal Records',
            },
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('games_file', models.FileField(upload_to='games')),
                ('games', models.JSONField(editable=False)),
                ('category', models.CharField(choices=[('PR', 'Premium'), ('FM', 'Fixed Matches'), ('VIP', 'VIP')], max_length=3)),
            ],
            options={
                'verbose_name_plural': 'Predictions',
            },
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('results', models.FileField(upload_to='results')),
                ('games', models.JSONField(editable=False)),
            ],
            options={
                'verbose_name_plural': 'Results',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('email', models.EmailField(max_length=32)),
                ('phone', models.CharField(max_length=13)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]