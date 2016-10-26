# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import concurrency.fields


class Migration(migrations.Migration):

    dependencies = [
        ('async', '0006_product_last_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='version',
            field=concurrency.fields.IntegerVersionField(default=1, help_text='record revision number'),
        ),
    ]
