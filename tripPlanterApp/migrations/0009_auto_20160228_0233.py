# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripPlanterApp', '0008_trip_issuggestedtrip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='picture',
            field=models.ImageField(upload_to=b'trip_images', blank=True),
        ),
    ]
