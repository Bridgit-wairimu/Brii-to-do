# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-02-03 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0011_task_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pictures/'),
        ),
    ]
