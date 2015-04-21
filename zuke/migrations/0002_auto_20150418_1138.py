# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zuke', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='device_1',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='devices',
            name='device_2',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='devices',
            name='device_3',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='devices',
            name='device_4',
            field=models.BooleanField(default=None),
        ),
    ]
