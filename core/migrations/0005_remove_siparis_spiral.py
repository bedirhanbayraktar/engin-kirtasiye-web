# Generated by Django 4.2.2 on 2023-06-25 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_siparis_cilt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siparis',
            name='spiral',
        ),
    ]
