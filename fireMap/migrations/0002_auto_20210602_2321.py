# Generated by Django 3.1.7 on 2021-06-02 23:21

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fireMap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incendio',
            name='coordenadas',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, default=None, null=True, srid=4326),
        ),
    ]
