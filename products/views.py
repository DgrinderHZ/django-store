from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
# Create your views here.

def say_hi(request, name):
    params = {'name': name}
    return render(request, 'say-hi.html', params)

def show_time(request):
    now = timezone.now()
    params = {'now': now}
    return render(request, 'show-time.html', params)

