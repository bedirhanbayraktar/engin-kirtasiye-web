# Generated by Django 4.1.5 on 2023-04-18 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_fotograf'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fotograf',
            options={'verbose_name_plural': 'Fotograflar'},
        ),
        migrations.AddField(
            model_name='fotograf',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fotograf',
            name='width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
