# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('playing_app', '0008_auto_20150717_1433'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Responsible',
        ),
        migrations.AlterField(
            model_name='todo',
            name='todo_responsibles',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
