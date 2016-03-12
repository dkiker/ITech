# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripPlanterApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='locationSlug',
            field=models.SlugField(default='glasgow'),
            preserve_default=False,
        ),
    ]
