import requests
from bs4 import BeautifulSoup
import json


def api_get(filters = [], fields = "" ,sort="id", reverse = 'false',results = 10, page=1,user='null',count='false',compact_filters = 'false',normalized_filters='false'):
    baseurl = 'https://api.vndb.org/kana/vn' 
    sendjson = { 
  "filters": filters, 
  "fields": fields,
  "sort": sort,
#  "reverse": reverse,
  "results": results,
  "page": page,
#  "user": 'null',
#  "count": count,
#  "compact_filters": compact_filters,
#  "normalized_filters": normalized_filters
}
    print(sendjson)
    response = requests.post(baseurl,json=sendjson)
    print(response)
    print(response.json())



        #for searching up tag names
    

api_get(filters = ["search", "=",'cyberpunk'], fields = "id")

#search_loopup()


