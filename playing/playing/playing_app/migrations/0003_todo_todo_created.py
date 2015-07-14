# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('playing_app', '0002_auto_20150609_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='todo_created',
            field=models.DateField(default=datetime.datetime(2015, 6, 15, 9, 45, 54, 886475, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
