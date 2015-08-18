# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('playing_app', '0012_auto_20150818_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='todo_created',
            field=models.DateField(null=True, default=datetime.datetime(2015, 8, 18, 9, 1, 31, 303764, tzinfo=utc)),
        ),
    ]
