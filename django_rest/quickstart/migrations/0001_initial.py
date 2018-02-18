# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-12 21:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Curs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('congnom_1', models.CharField(max_length=100)),
                ('congnom_2', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('data_naixement', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='assignatura',
            name='curs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curs', to='quickstart.Curs'),
        ),
        migrations.AddField(
            model_name='assignatura',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imparteix', to='quickstart.Professor'),
        ),
    ]
