# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar/default/default.jpg', upload_to='avatar/'),
        ),
    ]
