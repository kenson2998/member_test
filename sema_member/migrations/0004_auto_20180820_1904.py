# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-20 11:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sema_member', '0003_auto_20180820_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat1',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_chats', to=settings.AUTH_USER_MODEL),
        ),
    ]
