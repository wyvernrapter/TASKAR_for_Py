from django.shortcuts import render
from datetime import datetime
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.views.generic import ListView
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import RedirectView
from django.views import generic
from .models import Attendance
from django.utils import timezone
from datetime import datetime
from django.http import JsonResponse



class CustomLoginView(LoginView):
    template_name = 'Clock/custom_login.html'

    def get_success_url(self):
        user = self.request.user
        if user.is_superuser:
            return reverse_lazy('Clock:attendance')
        else:
            return reverse_lazy('Clock:attendance')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


def search_clear(request):
    if 'query' in request.session.keys():
        del request.session['query']
    if 'page' in request.session.keys():
        del request.session['page']
    return HttpResponseRedirect(reverse_lazy('index'))

class TransportCostView(generic.TemplateView):
    template_name = 'TransportCost.html'


class AttendanceTemplateView(generic.TemplateView):
    model = Attendance
    template_name = 'attendance.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.session = None

    def attendance(self, request):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        if 'start_time' not in request.session:
            request.session['start_time'] = current_time
            message = '出勤時間は{}です。'.format(current_time)
        else:
            end_time = current_time
            start_time = request.session.pop('start_time')
            message = '出勤時間は{}で、退勤時間は{}です。'.format(start_time, end_time)
        context = {'message': message, 'current_time': current_time}
        return render(request, '/a_index/index', context)

    def current_time(request):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return JsonResponse({'attendance.html': current_time})