# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripPlanterApp', '0004_auto_20160228_0036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='isSuggestedTrip',
        ),
    ]
