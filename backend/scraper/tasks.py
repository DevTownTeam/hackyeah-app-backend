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
    offers_list = BeautifulSoup(document, features='lxml') \
        .find('ul', {'class': 'results-list list-unstyled content'})

    for offer in filter(lambda s: s['href'][0] != '#', offers_list.find_all('a')):
        data = {}

        soup = BeautifulSoup(requests.get(offer['href']).text, features='lxml')

        data['name'] = soup.find('h1').string
        data['company'] = soup.find('div', {'class': 'company-name'}).string.strip()
        data['description'] = soup \
            .find('div', {'class': 'well well-shadow well-padded top-30'}) \
            .get_text() \
            .strip()

        result.append(data)

    return result
