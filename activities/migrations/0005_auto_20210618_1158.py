# Generated by Django 3.1 on 2021-06-18 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_auto_20210618_1052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='content_area_focus',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='earth_science_keyword',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='other_keyword',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='space_science_keyword',
        ),
    ]
