# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_remove_users_datehired'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='datehired',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
