# Generated by Django 3.2.5 on 2022-03-23 06:32

import Predictions.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Predictions', '0008_alter_multibetgames_games'),
    ]

    operations = [
        migrations.CreateModel(
            name='PopularGames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('games_file', models.FileField(upload_to='popular')),
                ('games', models.JSONField(editable=False)),
                ('home_logo', models.ImageField(default='', upload_to='popular-images')),
                ('away_logo', models.ImageField(default='', upload_to='popular-images')),
            ],
            options={
                'verbose_name_plural': 'Popular Games',
            },
        ),
        migrations.AlterField(
            model_name='multibetgames',
            name='games',
            field=Predictions.models.OldJSonField(blank=True, editable=False, null=True),
        ),
    ]
