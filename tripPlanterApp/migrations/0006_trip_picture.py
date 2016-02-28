# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tripPlanterApp', '0005_remove_trip_issuggestedtrip'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='picture',
            field=models.ImageField(default=datetime.date(2016, 2, 28), upload_to=b'trip_images', blank=True),
            preserve_default=False,
        ),
    ]
