# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-02-03 06:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0006_task_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
    ]
