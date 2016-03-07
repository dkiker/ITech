# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripPlanterApp', '0009_auto_20160228_0233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='picture',
            new_name='image',
        ),
    ]
