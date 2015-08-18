# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('playing_app', '0010_auto_20150813_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='todo_created',
            field=models.DateField(default=datetime.date(2015, 8, 18), null=True),
        ),
    ]
