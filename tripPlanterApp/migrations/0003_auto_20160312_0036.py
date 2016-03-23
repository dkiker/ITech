# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripPlanterApp', '0002_place_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='slug',
            new_name='locationSlug',
        ),
    ]
