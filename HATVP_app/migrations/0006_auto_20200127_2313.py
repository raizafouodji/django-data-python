# Generated by Django 2.2.5 on 2020-01-27 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HATVP_app', '0005_auto_20200127_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='level',
            field=models.CharField(choices=[('1', 'Local'), ('2', 'National'), ('3', 'Européen'), ('4', 'Mondial')], max_length=20, verbose_name='niveau_intervention'),
        ),
    ]
