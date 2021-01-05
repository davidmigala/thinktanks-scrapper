import json
import datetime
import requests

end_date=datetime.date.today()
start_date=(end_date - datetime.timedelta(days=14))
start_datetime = datetime.datetime.combine(start_date, datetime.datetime.min.time())
publisher='Baker Institute'

def get_data ():
    #Baker Institute principal
    results=[]
    url_base='https://s6.searchcdn.com/77d3d7d0562eef506e6ea07527cdb14e/mexico/0/539/?s=1609807824586&sort=doc_date&order=desc&resultCount=100'
    response=requests.get(url_base)
    page=response.text
    page=page.replace('addsearch.searchResults(', '')
    page=page.replace(');', '')
    documents=json.loads(page)
    articles=(documents['es']['hits']['hits'])
    for i, val in enumerate(articles):
        _date=datetime.datetime.strptime(val['fields']['doc_date'], '%Y-%m-%dT%H:%M:%S')
        if _date > start_datetime:
            if 'title' in val['fields']:
                _title=val['fields']['title']
            else:
                _title=val['fields']['url']
            myDict={
                'title': _title,
                'url': val['fields']['url'],
                'date': val['fields']['doc_date'],
                'publisher': publisher
            }
            results.append(myDict)
    return results

get_data()
