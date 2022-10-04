from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class HomePageView(LoginRequiredMixin, generic.ListView, TemplateView):
    template_name = 'home.html'


# Create your views here.

class ContactUsPageView(LoginRequiredMixin, generic.ListView, TemplateView):
    template_name = 'pages/contact-us.html'
