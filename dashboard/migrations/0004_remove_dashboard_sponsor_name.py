# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-31 21:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_dashboard_sponsor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboard',
            name='sponsor_name',
        ),
    ]