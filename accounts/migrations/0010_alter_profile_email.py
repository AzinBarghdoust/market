# Generated by Django 4.1.1 on 2022-10-15 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_customuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True, unique=True, verbose_name='ایمیل'),
        ),
    ]
