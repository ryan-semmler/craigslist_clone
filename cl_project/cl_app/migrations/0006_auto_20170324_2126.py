# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0005_posting_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='image',
            field=models.CharField(max_length=500),
        ),
    ]
