# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-16 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0004_curs_nivell'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitat',
            name='avaluable',
            field=models.BooleanField(default=True),
        ),
    ]