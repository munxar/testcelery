# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('async', '0005_auto_20161024_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 24, 19, 27, 25, 48480, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
