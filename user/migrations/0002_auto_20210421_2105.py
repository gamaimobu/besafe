# Generated by Django 3.1.7 on 2021-04-21 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='khach_hang',
            name='sdt',
            field=models.CharField(default='', max_length=15),
        ),
    ]