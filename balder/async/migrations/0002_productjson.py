# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('async', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductJson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.TextField()),
                ('last_modified', models.DateField(auto_now=True)),
                ('product', models.OneToOneField(to='async.Product')),
            ],
        ),
    ]
