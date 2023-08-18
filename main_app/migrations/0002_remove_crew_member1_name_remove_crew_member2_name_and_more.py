# Generated by Django 4.2.4 on 2023-08-18 20:09

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crew',
            name='member1_name',
        ),
        migrations.RemoveField(
            model_name='crew',
            name='member2_name',
        ),
        migrations.RemoveField(
            model_name='crew',
            name='member3_name',
        ),
        migrations.RemoveField(
            model_name='crew',
            name='member4_name',
        ),
        migrations.RemoveField(
            model_name='crew',
            name='member5_name',
        ),
        migrations.AddField(
            model_name='crew',
            name='members',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, null=True, size=5),
        ),
    ]
