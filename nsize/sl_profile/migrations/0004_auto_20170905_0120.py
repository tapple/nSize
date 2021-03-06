# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sl_profile', '0003_auto_20170904_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grid',
            name='hostname_suffix',
        ),
        migrations.AddField(
            model_name='grid',
            name='nick',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grid',
            name='region_domain',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='grid',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
