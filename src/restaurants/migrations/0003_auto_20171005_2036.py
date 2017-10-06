# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 20:36
from __future__ import unicode_literals

from django.db import migrations, models
import restaurants.validators


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20171005_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlocation',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True, validators=[restaurants.validators.validate_category]),
        ),
    ]
