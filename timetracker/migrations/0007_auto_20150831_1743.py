# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetracker', '0006_employee_manages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='manages',
        ),
        migrations.AddField(
            model_name='employee',
            name='manages',
            field=models.ForeignKey(blank=True, to='timetracker.Employee', null=True),
        ),
    ]
