# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-01 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0006_auto_20180501_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualificacio',
            name='qualificacio',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True),
        ),
    ]
