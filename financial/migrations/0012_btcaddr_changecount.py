# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-06 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0011_transaction_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='btcaddr',
            name='changeCount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
