from django.contrib import admin
from .models import Setting, Api


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('exchange',)


@admin.register(Api)
class APIAdmin(admin.ModelAdmin):
    list_display = ('api',)
