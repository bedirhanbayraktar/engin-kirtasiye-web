# Generated by Django 4.2.2 on 2023-06-25 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_siparis_cilt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siparis',
            name='cilt',
            field=models.CharField(default='Hiçbiri', max_length=20),
        ),
    ]
