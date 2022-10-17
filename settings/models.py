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


class API(models.Model):
    api = models.URLField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.api
