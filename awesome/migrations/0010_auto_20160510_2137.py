# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-10 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awesome', '0009_auto_20160510_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='website',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
