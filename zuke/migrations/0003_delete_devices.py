# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zuke', '0002_auto_20150418_1138'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Devices',
        ),
    ]
