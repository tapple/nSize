# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-09 18:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_auto_20170904_1752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='outfit',
            old_name='outfit_id',
            new_name='id',
        ),
    ]
