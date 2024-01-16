import requests
import json

#-1 will be for errors
def find_tags(instring):
    tagurl = 'https://api.vndb.org/kana/tag'
    tagrep = requests.post(tagurl,json={"filters": ["search", '=',instring],"fields":"id,name"})
    tagrep = tagrep.json()
    tagres = tagrep['results']
    if len(tagres) == 1:
        return tagres[0]['id']
    else:
        #multiple tags exist need better calirifiction
        print('more than one tag exists pick a correct name below')

        for i in range(len(tagres)):
            print(tagres[i]['name'])
        return -1





