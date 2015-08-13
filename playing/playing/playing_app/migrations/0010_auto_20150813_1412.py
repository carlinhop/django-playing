# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playing_app', '0009_auto_20150805_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='todo_created',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='todo_done',
            field=models.NullBooleanField(),
        ),
    ]
