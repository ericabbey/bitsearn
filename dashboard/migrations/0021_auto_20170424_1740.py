# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-24 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_dashboard_acc_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='acc_type',
            field=models.CharField(choices=[('u', 'ultimate'), ('d', 'dynamo'), ('p', 'prime'), ('n', 'normal')], default='n', max_length=1),
        ),
    ]
