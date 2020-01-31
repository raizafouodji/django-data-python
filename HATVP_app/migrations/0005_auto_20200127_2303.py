# Generated by Django 2.2.5 on 2020-01-27 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HATVP_app', '0004_auto_20200127_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalinformation',
            name='facebook',
            field=models.URLField(blank=True, max_length=500, verbose_name='page_facebook'),
        ),
        migrations.AlterField(
            model_name='generalinformation',
            name='linkedin',
            field=models.URLField(blank=True, max_length=500, verbose_name='page_linkedin'),
        ),
        migrations.AlterField(
            model_name='generalinformation',
            name='twitter',
            field=models.URLField(blank=True, max_length=500, verbose_name='page_twitter'),
        ),
        migrations.AlterField(
            model_name='generalinformation',
            name='website',
            field=models.URLField(blank=True, max_length=500, verbose_name='site_web'),
        ),
    ]
