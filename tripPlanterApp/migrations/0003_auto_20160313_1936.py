# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripPlanterApp', '0002_place_locationslug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='photograph',
            field=models.ImageField(default=b'media/trip_images/default.png', upload_to=b'trip_images', blank=True),
        ),
    ]
