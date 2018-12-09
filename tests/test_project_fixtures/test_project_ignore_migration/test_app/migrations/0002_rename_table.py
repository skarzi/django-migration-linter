# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 14:15
from __future__ import unicode_literals

from django.db import migrations

from django_migration_linter import IGNORE_MIGRATION


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_create_table'),
    ]

    operations = [
        migrations.RunSQL(IGNORE_MIGRATION),
        migrations.RenameModel(
            old_name='A',
            new_name='B',
        ),
    ]
