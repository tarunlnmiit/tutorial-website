# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-17 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_delete_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='inserted_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
