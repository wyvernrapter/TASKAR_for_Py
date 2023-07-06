from django.urls import path
from . import views

app_name = 'Transport'
urlpatterns = [
    path('Transport/', views.TransportCostView.as_view(), name='Transport')
]
