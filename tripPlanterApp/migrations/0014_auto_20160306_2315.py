# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripPlanterApp', '0013_place_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='location',
        ),
        migrations.RemoveField(
            model_name='place',
            name='type',
        ),
    ]
