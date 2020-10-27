# Generated by Django 3.1.2 on 2020-10-27 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journeycategorytranslation',
            name='master',
        ),
        migrations.RemoveField(
            model_name='journeychapter',
            name='activities',
        ),
        migrations.RemoveField(
            model_name='journeychapter',
            name='journey',
        ),
        migrations.AlterUniqueTogether(
            name='journeychaptertranslation',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='journeychaptertranslation',
            name='master',
        ),
        migrations.AddField(
            model_name='activitytranslation',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='pdf/'),
        ),
        migrations.DeleteModel(
            name='JourneyCategory',
        ),
        migrations.DeleteModel(
            name='JourneyCategoryTranslation',
        ),
        migrations.DeleteModel(
            name='JourneyChapter',
        ),
        migrations.DeleteModel(
            name='JourneyChapterTranslation',
        ),
    ]