# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripPlanterApp', '0010_auto_20160306_2103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='image',
            new_name='picture',
        ),
    ]
