# Generated by Django 3.1 on 2021-06-18 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='spaceawe_node',
        ),
        migrations.RemoveField(
            model_name='person',
            name='spaceawe_partner',
        ),
    ]
