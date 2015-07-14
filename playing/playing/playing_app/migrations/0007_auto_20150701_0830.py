# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playing_app', '0006_auto_20150630_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsible',
            name='responsible_name',
            field=models.CharField(max_length=200),
        ),
    ]
