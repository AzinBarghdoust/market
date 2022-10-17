from django.urls import path
from . import views

urlpatterns = [
    path('', views.settings, name='settings'),
    path('api/', views.api, name='api'),
    path('api/trade', views.trade, name='trade'),

]
