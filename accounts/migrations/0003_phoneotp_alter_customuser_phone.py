# Generated by Django 4.1.1 on 2022-10-03 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneOTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11, null=True)),
                ('otp', models.IntegerField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(help_text='Enter 11 digits phone number', max_length=11, unique=True, verbose_name='شماره موبایل'),
        ),
    ]