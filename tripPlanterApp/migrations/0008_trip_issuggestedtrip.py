# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripPlanterApp', '0007_auto_20160228_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='isSuggestedTrip',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
