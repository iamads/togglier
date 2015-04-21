# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_1', models.BooleanField()),
                ('device_2', models.BooleanField()),
                ('device_3', models.BooleanField()),
                ('device_4', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
