# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RedditCryptoCount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lastcount',
            name='pc_diff',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='lastcount',
            name='lastcount',
            field=models.IntegerField(null=True),
        ),
    ]
