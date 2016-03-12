# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=2, choices=[(b'A', b'Attraction'), (b'H', b'Hotel'), (b'R', b'Restaurant')])),
                ('location', models.CharField(max_length=20)),
                ('lat', models.DecimalField(max_digits=9, decimal_places=6, blank=True)),
                ('lon', models.DecimalField(max_digits=9, decimal_places=6, blank=True)),
                ('price', models.IntegerField(blank=True)),
                ('description', models.CharField(default=b'', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Planner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=128, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('photograph', models.ImageField(upload_to=b'trip_images', blank=True)),
                ('isSuggestedTrip', models.BooleanField(default=False)),
                ('planner', models.ForeignKey(to='tripPlanterApp.Planner')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place', models.ForeignKey(to='tripPlanterApp.Place')),
                ('trip', models.ForeignKey(to='tripPlanterApp.Trip')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
