# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripPlanterApp', '0011_auto_20160306_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='type',
            field=models.CharField(default='r', max_length=1, choices=[(b'R', b'Restaurant'), (b'H', b'Hotel'), (b'A', b'Attraction')]),
            preserve_default=False,
        ),
    ]
