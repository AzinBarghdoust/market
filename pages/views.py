from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class HomePageView(TemplateView):
    template_name = 'home.html'


# Create your views here.

class ContactUsPageView(TemplateView):
    template_name = 'pages/contactus.html'


def teach(request):
    return render(request, 'pages/teach.html')


