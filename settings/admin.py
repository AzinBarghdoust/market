from django.contrib import admin
from .models import Setting, API


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('exchange',)


@admin.register(API)
class APIAdmin(admin.ModelAdmin):
    list_display = ('api',)
