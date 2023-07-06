from django.urls import path
from . import views

app_name = 'Clock'
urlpatterns = [
    path('index/', views.AttendanceTemplateView.as_view(), name='index'),
    path('Transport/', views.TransportCostView.as_view(), name='Transport')
]
