# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetracker', '0010_auto_20150831_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='manages',
            field=models.ManyToManyField(to='timetracker.Employee', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='projects',
            field=models.ManyToManyField(to='timetracker.Project', blank=True),
        ),
    ]
