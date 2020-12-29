import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date, timedelta

end_date = date.today()
start_date=(end_date - timedelta(days=14))
publisher='AEI'

def get_data():
    #aei.org principal
    results=[]
    start_datetime=start_date.strftime('%m/%d/%Y')
    end_datetime=end_date.strftime('%m/%d/%Y')
    url_base=f'https://www.aei.org/search-results/?wpsolr_q=mexico&wpsolr_start_date={start_datetime}&wpsolr_end_date={end_datetime}'
    response=requests.get(url_base)
    page=BeautifulSoup(response.text, 'html.parser')
    href_titles=page.find_all('h4', class_='entry-title')
    authors=page.find_all('a', class_='author-link')
    dates=page.find_all('span', class_='primary-18')
    for i, val in enumerate(href_titles):
        myDict={
            'title': val.a.get_text(),
            'url': val.a.get('href'),
            'author': authors[i].get_text(),
            'date': dates[i].get_text(),
            'publisher': publisher
        }
        results.append(myDict)

    return results
