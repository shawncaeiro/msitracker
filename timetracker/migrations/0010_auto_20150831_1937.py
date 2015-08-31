# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetracker', '0009_auto_20150831_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
        migrations.AlterField(
            model_name='employee',
            name='projects',
            field=models.ManyToManyField(to='timetracker.Project', null=True, blank=True),
        ),
    ]
