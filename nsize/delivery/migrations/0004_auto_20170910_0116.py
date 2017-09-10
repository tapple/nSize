# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-10 01:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_auto_20170909_1844'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='deliveryrequest',
            name='delivery_re_grid_id_67cd04_idx',
        ),
        migrations.RemoveIndex(
            model_name='deliveryrequest',
            name='delivery_re_grid_id_58ee63_idx',
        ),
        migrations.RenameField(
            model_name='deliveryrequest',
            old_name='fiscal_day',
            new_name='fiscal_date',
        ),
        migrations.AddIndex(
            model_name='deliveryrequest',
            index=models.Index(fields=['grid', 'fiscal_date', 'creator'], name='delivery_re_grid_id_e271e6_idx'),
        ),
        migrations.AddIndex(
            model_name='deliveryrequest',
            index=models.Index(fields=['grid', 'creator', 'fiscal_date'], name='delivery_re_grid_id_b10de9_idx'),
        ),
    ]
