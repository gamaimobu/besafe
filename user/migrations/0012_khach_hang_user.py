# Generated by Django 3.1.7 on 2021-05-02 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0011_remove_khach_hang_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='khach_hang',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
