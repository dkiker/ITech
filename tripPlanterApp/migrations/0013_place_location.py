# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripPlanterApp', '0012_place_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='location',
            field=models.CharField(default='glasgow', max_length=20),
            preserve_default=False,
        ),
    ]
