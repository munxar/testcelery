# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('async', '0004_auto_20161024_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productjson',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='productjson',
            name='product',
            field=models.OneToOneField(related_name='product_json', to='async.Product'),
        ),
    ]
