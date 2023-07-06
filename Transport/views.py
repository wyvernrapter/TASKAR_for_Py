from django.shortcuts import render
from django.views import generic
# Create your views here.

class TransportCostView(generic.TemplateView):
    template_name = 'TransportCost.html'

