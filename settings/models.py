import datetime
from datetime import timezone

from django.db import models
from accounts.models import CustomUser


class Setting(models.Model):
    STATUS_CHOICES = (
        ('kucoin', 'Kucoin'),
        ('binance', 'Binance'),
        ('nobitex', 'Nobitex')
    )

    exchange = models.CharField(choices=STATUS_CHOICES, max_length=12, verbose_name='صرافی', default='Kucoin')

    def __str__(self):
        return self.exchange


class Api(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    api = models.URLField(max_length=200)

    def __str__(self):
        return self.api
