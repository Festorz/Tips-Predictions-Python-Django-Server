# Generated by Django 3.2.5 on 2022-03-26 14:00

import Predictions.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Predictions', '0010_alter_multibetgames_games'),
    ]

    operations = [
        migrations.AlterField(
            model_name='populargames',
            name='games',
            field=Predictions.models.OldJSonField(editable=False),
        ),
    ]
