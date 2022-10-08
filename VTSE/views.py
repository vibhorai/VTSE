# @Author - Vibhor Chander

from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    params = {'name': 'Vibhor'}
    return render(request, 'index.html',params)

