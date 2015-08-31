# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('timetracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='timesheet',
            name='fri',
        ),
        migrations.RemoveField(
            model_name='timesheet',
            name='mon',
        ),
        migrations.RemoveField(
            model_name='timesheet',
            name='sat',
        ),
        migrations.RemoveField(
            model_name='timesheet',
            name='sun',
        ),
        migrations.RemoveField(
            model_name='timesheet',
            name='thurs',
        ),
        migrations.RemoveField(
            model_name='timesheet',
            name='tues',
        ),
        migrations.RemoveField(
            model_name='timesheet',
            name='user',
        ),
        migrations.RemoveField(
            model_name='timesheet',
            name='wed',
        ),
        migrations.RemoveField(
            model_name='timesheet',
            name='week',
        ),
        migrations.AddField(
            model_name='timesheet',
            name='date',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
        migrations.AddField(
            model_name='timesheet',
            name='employee',
            field=models.ForeignKey(default=None, to='timetracker.Employee', null=True),
        ),
        migrations.AddField(
            model_name='timesheet',
            name='hours',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='projects',
            field=models.ManyToManyField(to='timetracker.Project'),
        ),
        migrations.AddField(
            model_name='timesheet',
            name='project',
            field=models.ForeignKey(default=None, to='timetracker.Project', null=True),
        ),
    ]
