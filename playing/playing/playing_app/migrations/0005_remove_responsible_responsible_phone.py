# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playing_app', '0004_auto_20150630_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responsible',
            name='responsible_phone',
        ),
    ]
