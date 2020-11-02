from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def say_hi(request, name):
    params = {'name': name}
    return render(request, 'say-hi.html', params)
