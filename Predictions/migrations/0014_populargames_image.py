# Generated by Django 3.2.5 on 2022-03-28 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Predictions', '0013_alter_populargames_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='populargames',
            name='image',
            field=models.ImageField(default='', upload_to='popular-images'),
        ),
    ]
