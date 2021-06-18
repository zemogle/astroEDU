# Generated by Django 3.1 on 2021-06-18 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_auto_20210518_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='affiliation',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='country',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='email',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='language',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='max_number_at_once',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='suitable_group_size',
        ),
        migrations.RemoveField(
            model_name='activitytranslation',
            name='big_idea',
        ),
        migrations.RemoveField(
            model_name='activitytranslation',
            name='spaceawe_authorship',
        ),
        migrations.AlterField(
            model_name='activitytranslation',
            name='abstract',
            field=models.TextField(blank=True, help_text='200 words', verbose_name='Abstract'),
        ),
    ]
