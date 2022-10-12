from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('contactus', views.ContactUsPageView.as_view(), name='contactus'),
    path('teach', views.teach, name='teach'),
]
