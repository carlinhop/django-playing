# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playing_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responsibilities',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Responsible',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('responsible_name', models.CharField(max_length=200)),
                ('responsible_phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='responsibilities',
            name='responsible',
            field=models.ManyToManyField(to='playing_app.Responsible'),
        ),
        migrations.AddField(
            model_name='responsibilities',
            name='task',
            field=models.ManyToManyField(to='playing_app.Todo'),
        ),
    ]
