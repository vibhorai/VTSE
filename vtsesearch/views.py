from gettext import translation
from django.http import HttpResponse
from django.shortcuts import render


from .documents import CarDocument,VedicTextDocument
from elasticsearch_dsl import Q
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from .models import Car,VedicText
from .search import BGIndex
from . import models
from django.core.paginator import Paginator


# Create your views here.


def search(request):
    searchText = request.GET.get('searchText','default')
    #q = Q(
    # 'match_phrase',
    # translation=searchText)
    q = Q(
     'multi_match',
     query=searchText,
     fields=[
         'title',
         'translation'
     ],
     fuzziness= "AUTO")
    
    
    
    
    page_number = int(request.GET.get('page','1'))
    
    start = (page_number-1) * 10
    end = start + 10
    
    search = VedicTextDocument.search().query(q)[start:end]
   
    
    
    
    p = Paginator(search, 10)
    
    
    try:
        page_obj = p.get_page(page_number) 
        
        
    except PageNotAnInteger:
        
        page_obj = p.page(1)

        
        
    except EmptyPage:
        
        page_obj = p.page(p.num_pages)
        
        
    
    context = {'page_obj': page_obj, 'searchText':searchText}
    
    
    return render(request, 'searchResults.html',context)