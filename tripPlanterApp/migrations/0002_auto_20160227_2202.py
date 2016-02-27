# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripPlanterApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='lat',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='place',
            name='lon',
            field=models.IntegerField(),
        ),
    ]
