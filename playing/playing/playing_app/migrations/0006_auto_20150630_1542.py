# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playing_app', '0005_remove_responsible_responsible_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsible',
            name='responsible_name',
            field=models.CharField(default='Nothing', max_length=200),
        ),
    ]
