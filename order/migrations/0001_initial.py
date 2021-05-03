# Generated by Django 3.1.7 on 2021-04-21 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Don_dat_hang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngay_dat', models.DateField()),
                ('ngay_giao', models.DateField()),
                ('so_luong', models.IntegerField()),
                ('tinh_trang', models.CharField(default='', max_length=50)),
                ('hinh_thuc_thanh_toan', models.CharField(default='', max_length=100)),
                ('khach_hang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.khach_hang')),
                ('san_pham', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.san_pham')),
            ],
        ),
    ]