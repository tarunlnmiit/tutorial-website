# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-17 09:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170617_1433'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]