# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-30 08:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kdnote_site', '0002_auto_20171230_1653'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='admin',
            new_name='is_admin',
        ),
    ]