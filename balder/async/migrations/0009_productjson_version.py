# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import concurrency.fields


class Migration(migrations.Migration):

    dependencies = [
        ('async', '0008_auto_20161024_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='productjson',
            name='version',
            field=concurrency.fields.AutoIncVersionField(default=1, help_text='record revision number'),
        ),
    ]
