# Generated by Django 3.2.5 on 2022-03-09 13:32

import django.contrib.postgres.fields.hstore
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Predictions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multibetgames',
            name='games',
            field=django.contrib.postgres.fields.hstore.HStoreField(editable=False),
        ),
    ]
