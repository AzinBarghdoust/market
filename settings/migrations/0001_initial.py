# Generated by Django 4.1.1 on 2022-10-09 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange', models.CharField(choices=[('kucoin', 'Kucoin'), ('binance', 'Binance'), ('nobitex', 'Nobitex')], default='Kucoin', max_length=12, verbose_name='صرافی')),
            ],
        ),
    ]
