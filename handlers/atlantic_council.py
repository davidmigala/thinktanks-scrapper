import json
import time
import requests
import pandas as pd

current_time=time.time()
start_date=current_time - (60 * 60 * 24 * 14) # 14 days in seconds
publisher='Atlantic Council'

def get_data():
    #atlanticcouncil.org principal
    results=[]
    url_base='https://nh6cusbog5-dsn.algolia.net/1/indexes/atlantic-council-search/query?x-algolia-agent=Algolia%20for%20JavaScript%20(3.35.1)%3B%20Browser&x-algolia-application-id=NH6CUSBOG5&x-algolia-api-key=0c875d2890391a0fdc947f4e5a175911'
    payload={
        'params': 'query=mexico&filters=%20focus%3Aevents%20OR%20focus%3Ablogs%20OR%20focus%3Ainsight-impact&hitsPerPage=100&page=0'
    }
    response=requests.post(url_base, data=json.dumps(payload))
    response_body=json.loads(response.text)
    articles=response_body['hits']
    for article in articles:
        if (start_date < article['timestamp']):
            author=article['author']['name'] if len(article['author']) > 0 else ''
            myDict={
                'url': article['url'],
                'date': article['date'],
                'title': article['title'],
                'author': author,
                'publisher': publisher
            }
            results.append(myDict)

    return results
