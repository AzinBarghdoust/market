# Generated by Django 4.1.1 on 2022-10-08 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=20, verbose_name='استان'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=200, unique=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(1, 'مرد'), (2, 'زن')], null=True, verbose_name='جنسیت'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='نام خانوادگی'),
        ),
    ]
