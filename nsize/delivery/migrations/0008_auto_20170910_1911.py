# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-10 19:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0007_auto_20170910_1746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='outfit',
            old_name='garments',
            new_name='components',
        ),
    ]
