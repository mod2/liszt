# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liszt', '0007_item_starred'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='starred_order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='list',
            name='starred_order',
            field=models.IntegerField(default=0),
        ),
    ]