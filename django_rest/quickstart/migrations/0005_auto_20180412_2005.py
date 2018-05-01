# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-12 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0004_grup_centre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curs',
            name='nivell',
            field=models.CharField(choices=[('ESO', 'ESO'), ('Batxillerat', 'Batxillerat')], max_length=15),
        ),
        migrations.AlterField(
            model_name='professor',
            name='email',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]