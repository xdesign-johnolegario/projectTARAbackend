# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-27 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptaraback', '0003_auto_20180227_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ptarausers',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
