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


def parse_bulldog(document, only_one=False):
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

        tech_tags = soup.find('div', {'class': 'row technologies flex flex-stretch flex-wrap flex-desktop'})
        data['technologies'] = [
            tech.get_text().strip()
            for tech in tech_tags
                .find_all('span')
        ][::2] if tech_tags else None

        salary_element = soup.find('div', {'class': 'money'})
        salary_string = salary_element.string.replace(' ', '').split('-') if salary_element else None
        if salary_string:
            data['salary_lower'] = salary_string[0]
            data['salary_upper'] = salary_string[1] if len(salary_string) == 2 else salary_string[0]
        else:
            data['salary_lower'] = None
            data['salary_upper'] = None

        result.append(data)

        if only_one:
            break

    return result
