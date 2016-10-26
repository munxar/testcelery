# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('async', '0002_productjson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productjson',
            name='product',
            field=models.OneToOneField(related_name='product_json', to='async.Product'),
        ),
    ]
