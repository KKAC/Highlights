# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-13 12:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fb_highlights', '0029_auto_20180402_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latesthighlight',
            name='category',
            field=models.ForeignKey(db_column='category', on_delete=django.db.models.deletion.CASCADE, to='fb_highlights.FootballCompetition'),
        ),
    ]
