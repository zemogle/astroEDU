# Generated by Django 2.2.14 on 2020-08-05 13:53

from django.db import migrations, models
import django.db.models.deletion
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SmartEmbed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, db_index=True, help_text='Internal code to identify the embed; if set, do not modify. When in doubt, leave empty.', max_length=100, unique=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modification_date', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'embed',
                'ordering': ('code',),
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SmartPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured', models.BooleanField(default=False)),
                ('published', models.BooleanField(default=True)),
                ('release_date', models.DateTimeField()),
                ('embargo_date', models.DateTimeField(blank=True, null=True)),
                ('code', models.CharField(blank=True, db_index=True, help_text='Internal code to identify the page; if set, do not modify. When in doubt, leave empty.', max_length=100, unique=True)),
                ('registration_required', models.BooleanField(default=False, help_text='If this is checked, only logged-in users will be able to view the page.', verbose_name='registration required')),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modification_date', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'page',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SmartPageTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('url', models.CharField(db_index=True, help_text='Example: "/about/contact/". Make sure to have leading and trailing slashes.', max_length=100, verbose_name='URL')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('content', models.TextField(blank=True, verbose_name='content')),
                ('master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='smartpages.SmartPage')),
            ],
            options={
                'verbose_name': 'page translation',
                'unique_together': {('language_code', 'master'), ('language_code', 'url')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SmartEmbedTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('content', models.TextField(blank=True, verbose_name='content')),
                ('master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='smartpages.SmartEmbed')),
            ],
            options={
                'verbose_name': 'embed translation',
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
