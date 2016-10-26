# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import concurrency.fields


class Migration(migrations.Migration):

    dependencies = [
        ('async', '0007_product_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='version',
            field=concurrency.fields.AutoIncVersionField(default=1, help_text='record revision number'),
        ),
    ]
