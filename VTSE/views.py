# @Author - Vibhor Chander

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name': 'Vibhor'}
    return render(request, 'index.html',params)

def search(request):
    searchText = request.GET.get('searchText','default')
    print('Search Text is ', searchText)
    params = {'searchedText': searchText}
    return render(request, 'searchResults.html',params)