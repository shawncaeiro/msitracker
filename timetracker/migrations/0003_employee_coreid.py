# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetracker', '0002_auto_20150828_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='coreid',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
