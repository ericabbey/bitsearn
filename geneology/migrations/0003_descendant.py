# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-12 16:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('geneology', '0002_auto_20170401_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descendant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('downliner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child', to=settings.AUTH_USER_MODEL)),
                ('upliner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upliner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
