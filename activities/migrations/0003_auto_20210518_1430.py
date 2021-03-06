# Generated by Django 3.1 on 2021-05-18 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_auto_20201027_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitytranslation',
            name='abstract',
            field=models.TextField(blank=True, help_text='250 chars', verbose_name='Abstract'),
        ),
        migrations.AlterField(
            model_name='activitytranslation',
            name='pdf',
            field=models.FileField(blank=True, help_text='PDF will be autogenerated after publication. Do not upload one.', null=True, upload_to='pdf/'),
        ),
        migrations.AlterField(
            model_name='activitytranslation',
            name='teaser',
            field=models.TextField(help_text='250 chars', verbose_name='Teaser'),
        ),
        migrations.AlterField(
            model_name='metadataoption',
            name='group',
            field=models.CharField(choices=[('age', 'Age'), ('level', 'Level'), ('time', 'Time'), ('group', 'Group'), ('supervised', 'Supervised'), ('cost', 'Cost per student'), ('location', 'Location'), ('skills', 'Core skills'), ('learning', 'Type(s) of learning activity'), ('content_area_focus', 'Content Area focus'), ('astronomical_scientific_category', 'Astronomy Categories'), ('earth_science_keyword', 'Earth Science keywords'), ('space_science_keyword', 'Space Science keywords')], max_length=50),
        ),
    ]
