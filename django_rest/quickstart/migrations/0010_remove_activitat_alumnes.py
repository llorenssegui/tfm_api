# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-20 18:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0009_auto_20180220_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitat',
            name='alumnes',
        ),
    ]
