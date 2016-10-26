# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('async', '0003_auto_20161024_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productjson',
            name='product',
            field=models.OneToOneField(to='async.Product'),
        ),
    ]
