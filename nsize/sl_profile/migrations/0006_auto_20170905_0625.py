# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 06:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sl_profile', '0005_grid_table_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resident',
            old_name='user_name',
            new_name='name',
        ),
    ]