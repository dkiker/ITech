# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripPlanterApp', '0018_auto_20160306_2330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='picture',
            new_name='photograph',
        ),
    ]
