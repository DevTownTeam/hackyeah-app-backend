import requests
from bs4 import BeautifulSoup
from celery import shared_task


@shared_task
def scrape(url):
    result = requests.get(url)
    offers = []
    if 'bulldogjob.pl' in url:
        offers = parse_bulldog(result.text)

    return offers


def parse_bulldog(document):
    result = []
    offers_list = BeautifulSoup(document) \
        .find('ul', {'class': 'results-list list-unstyled content'})

    for offer in offers_list.find_all('a'):
        data = {}

        soup = BeautifulSoup(requests.get(offer['href']).text)

        data['name'] = soup.find('h1').string
        data['company'] = soup.find('div', {'class': 'company-name'}).string.strip()

        result.append(data)

    return result
