# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-14 19:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fb_highlights', '0030_auto_20180413_1200'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewFootballTeam',
            new_name='NewFootballRegistration',
        ),
        migrations.DeleteModel(
            name='NewFootballCompetition',
        ),
    ]
