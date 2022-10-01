from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('contact-us.html', views.ContactUsPageView.as_view(), name='contactus'),
]