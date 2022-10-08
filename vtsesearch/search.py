from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Document, Text, Date, Search
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

# Create a connection to ElasticSearch
connections.create_connection()

# ElasticSearch "model" mapping out what fields to index

class BGIndex(Document):
    translation = Text()
    title = Text()
    url = Text()

    class Index:
      name = 'bg-supersite'

# Bulk indexing function, run in shell
def bulk_indexing():
    BGIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.VedicText.objects.all().iterator()))

# Simple search function
def search():
    s = Search().filter('term', title="Bhagavad Geeta chapter 1 shloka 1")
    response = s.execute()
    return response