# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-10 17:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0004_auto_20170910_0116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliveryrequest',
            old_name='avatar',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='garment',
            old_name='avatar',
            new_name='body',
        ),
    ]