# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-20 11:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sema_member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sema_member.Employees')),
            ],
        ),
    ]