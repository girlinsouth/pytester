# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pybugs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('remarks', models.TextField()),
                ('project', models.IntegerField()),
                ('module', models.IntegerField()),
                ('creater', models.IntegerField()),
                ('ccer', models.IntegerField()),
                ('assigner', models.IntegerField()),
                ('fixer', models.IntegerField()),
                ('fixTime', models.DateTimeField()),
                ('fixWay', models.IntegerField()),
                ('closer', models.IntegerField()),
                ('priority', models.IntegerField()),
                ('serious', models.IntegerField()),
                ('closeTime', models.DateTimeField()),
                ('createTime', models.DateTimeField()),
                ('updateTime', models.DateTimeField()),
                ('duplicateID', models.IntegerField()),
                ('relatedBugID', models.IntegerField()),
                ('relatedCaseID', models.IntegerField()),
                ('file', models.FileField(upload_to=b'./upload/')),
                ('status', models.IntegerField()),
            ],
        ),
    ]
