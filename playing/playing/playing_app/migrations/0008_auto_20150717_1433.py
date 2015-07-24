# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playing_app', '0007_auto_20150701_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='todo_created',
            field=models.DateField(),
        ),
    ]
