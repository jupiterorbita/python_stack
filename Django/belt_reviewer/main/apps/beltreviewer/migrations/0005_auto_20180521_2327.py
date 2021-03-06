# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-21 23:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beltreviewer', '0004_auto_20180521_1552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='book_review',
            new_name='book',
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='beltreviewer.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
