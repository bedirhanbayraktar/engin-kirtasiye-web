# Generated by Django 4.1.5 on 2023-04-22 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_siparis_isim_soyisim_alter_siparis_telefon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siparis',
            name='isim_soyisim',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='telefon',
            field=models.CharField(max_length=15),
        ),
    ]
