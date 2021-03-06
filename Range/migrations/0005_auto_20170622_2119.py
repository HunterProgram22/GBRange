# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-23 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Range', '0004_auto_20170620_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drill_base_model',
            name='level',
        ),
        migrations.AlterField(
            model_name='drill_base_model',
            name='area',
            field=models.CharField(choices=[('Woods', 'Woods'), ('Hybrids', 'Hybrids'), ('Irons', 'Irons'), ('Wedges', 'Wedges'), ('Chipping', 'Chipping'), ('Putting', 'Putting')], max_length=50),
        ),
        migrations.AlterField(
            model_name='drill_base_model',
            name='club',
            field=models.CharField(choices=[('Driver', 'Driver'), ('3 Wood', 'Three Wood'), ('3 Hybrid', '3 Hybrid'), ('5 Iron', '5 Iron'), ('6 Iron', '6 Iron'), ('7 Iron', '7 Iron'), ('8 Iron', '8 Iron'), ('9 Iron', '9 Iron'), ('Pitch Wedge 45', 'Pitching Wedge 45'), ('Gap Wedge 50', 'Gap Wedge 50'), ('Sand Wedge 54', 'Sand Wedge 54'), ('Lob Wedge 58', 'Lob Wedge 58'), ('Putter', 'Putter')], max_length=25),
        ),
        migrations.AlterField(
            model_name='drill_base_model',
            name='detail',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='drill_base_model',
            name='drill',
            field=models.CharField(choices=[('CS', 'Center Face Hit'), ('AA', 'Upward Angle of Attack'), ('CP', 'Club Face and Path')], max_length=50),
        ),
        migrations.AlterField(
            model_name='drill_base_model',
            name='shots_success',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
