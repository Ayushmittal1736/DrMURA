# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-20 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identify', '0003_auto_20190420_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xray',
            name='probability',
            field=models.CharField(max_length=10),
        ),
    ]
