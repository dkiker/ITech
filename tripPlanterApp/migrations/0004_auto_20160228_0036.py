# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripPlanterApp', '0003_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='isSuggestedTrip',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='place',
            name='lat',
            field=models.DecimalField(max_digits=9, decimal_places=6, blank=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='lon',
            field=models.DecimalField(max_digits=9, decimal_places=6, blank=True),
        ),
    ]
