# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-19 23:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fb_highlights', '0019_auto_20180219_2210'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='highlightnotificationstat',
            unique_together=set([('user', 'send_time_2')]),
        ),
        migrations.RemoveField(
            model_name='highlightnotificationstat',
            name='open_time',
        ),
        migrations.RemoveField(
            model_name='highlightnotificationstat',
            name='send_time',
        ),
    ]