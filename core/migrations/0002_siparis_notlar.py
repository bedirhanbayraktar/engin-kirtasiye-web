# Generated by Django 4.2.2 on 2023-06-25 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='siparis',
            name='notlar',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]