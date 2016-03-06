# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripPlanterApp', '0014_auto_20160306_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='location',
            field=models.CharField(default='Glasgow', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='type',
            field=models.CharField(default='Attraction', max_length=2, choices=[(b'A', b'Attraction'), (b'H', b'Hotel'), (b'R', b'Restaurant')]),
            preserve_default=False,
        ),
    ]
