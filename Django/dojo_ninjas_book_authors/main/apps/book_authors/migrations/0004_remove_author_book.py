# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-17 21:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0003_auto_20180517_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='book',
        ),
    ]