from django.http import HttpResponse
from django.shortcuts import render
from .documents import CarDocument,VedicTextDocument
from elasticsearch_dsl import Q
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from .models import Car,VedicText
from .search import BGIndex
from . import models

# Create your views here.


def search(request):
    searchText = request.GET.get('searchText','default')
    print('I am here')
    #car = Car(name="Car one",color="red",type=1,description="A beautiful car")
    #car.save()
    #s = CarDocument.search().filter("term", color="red")
    #vt = VedicText(title="Car one",url="red",translation="A beautiful car")
    #vt.save()
    #s = VedicTextDocument.search().filter('term', title="Bhagavad Geeta chapter 1 shloka 1")
    #s = BGIndex.search()
    #es = Elasticsearch()
    #bulk(client=es, actions=(b.indexing() for b in models.VedicText.objects.all().iterator()))
    query = 'Bhagavad Geeta chapter 1 shloka 1'
    q = Q(
     'match_phrase',
     title=searchText)
    search = VedicTextDocument.search().query(q)
    #response = search.execute()

# print all the hits
    #for hit in search:
    #    print("Title : {}, Translation {}".format(hit.title, hit.translation))
        
    
    params = {'searchedText': search}
    return render(request, 'searchResults.html',params)