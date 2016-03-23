# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripPlanterApp', '0003_auto_20160313_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='photograph',
            field=models.ImageField(default=b'trip_images/default.png', upload_to=b'trip_images', blank=True),
        ),
    ]
