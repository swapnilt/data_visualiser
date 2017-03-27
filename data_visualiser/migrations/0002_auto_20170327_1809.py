# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-03-27 12:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_visualiser', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maxtempdata',
            options={'verbose_name': 'Max Temperature Data', 'verbose_name_plural': 'Max Temperature Data'},
        ),
        migrations.AlterModelOptions(
            name='meantempdata',
            options={'verbose_name': 'Mean Temperature Data', 'verbose_name_plural': 'Mean Temperature Data'},
        ),
        migrations.AlterModelOptions(
            name='mintempdata',
            options={'verbose_name': 'Min Temperature Data', 'verbose_name_plural': 'Min Temperature Data'},
        ),
        migrations.AlterModelOptions(
            name='raindata',
            options={'verbose_name': 'Rain Data', 'verbose_name_plural': 'Rain Data'},
        ),
        migrations.AlterModelOptions(
            name='sunshinedata',
            options={'verbose_name': 'Sunshine Data', 'verbose_name_plural': 'Sunshine Data'},
        ),
    ]
