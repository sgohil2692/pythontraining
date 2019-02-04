# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('firstapplication', '0003_auto_20190131_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.CharField(default=datetime.datetime(2019, 2, 4, 3, 38, 44, 633000, tzinfo=utc), unique=True, max_length=100),
            preserve_default=False,
        ),
    ]
