# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetracker', '0007_auto_20150831_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='manages',
        ),
        migrations.AddField(
            model_name='employee',
            name='manages',
            field=models.ManyToManyField(related_name='manages_rel_+', null=True, to='timetracker.Employee', blank=True),
        ),
    ]
