# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybug', '0002_auto_20150827_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pybugs',
            name='fixWay',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pybugs',
            name='priority',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pybugs',
            name='serious',
            field=models.CharField(max_length=20),
        ),
    ]
