# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playing_app', '0003_todo_todo_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responsibilities',
            name='responsible',
        ),
        migrations.RemoveField(
            model_name='responsibilities',
            name='task',
        ),
        migrations.AddField(
            model_name='todo',
            name='todo_responsibles',
            field=models.ManyToManyField(to='playing_app.Responsible'),
        ),
        migrations.DeleteModel(
            name='Responsibilities',
        ),
    ]
