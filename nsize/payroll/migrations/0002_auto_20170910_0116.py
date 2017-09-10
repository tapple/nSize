# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-10 01:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sl_profile', '0007_auto_20170907_1449'),
        ('payroll', '0001_initial'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='transaction',
            name='payroll_tra_grid_id_efd639_idx',
        ),
        migrations.RenameField(
            model_name='dayledger',
            old_name='fiscal_day',
            new_name='fiscal_date',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='fiscal_day',
            new_name='fiscal_date',
        ),
        migrations.AlterUniqueTogether(
            name='dayledger',
            unique_together=set([('grid', 'fiscal_date')]),
        ),
        migrations.AddIndex(
            model_name='transaction',
            index=models.Index(fields=['grid', 'fiscal_date', 'resident'], name='payroll_tra_grid_id_90117a_idx'),
        ),
    ]
