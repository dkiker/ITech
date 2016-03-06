# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripPlanterApp', '0015_auto_20160306_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='description',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
    ]
