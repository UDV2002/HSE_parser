import requests
from bs4 import BeautifulSoup
# from flask import Flask
# from flask_restful import Api, Resource
# import csv

HOST = "https://www.hse.ru/"
HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,imag" +
              "e/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " +
                  "Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84 (Edition Yx 08)"
}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    print(f"\nConnection with {url}:\nSuccessful\nhtml object is ready to work with...\n")
    return r


def get_faculties(params=''):
    url = HOST + "education/faculty/"
    html = get_html(url, params=params)
    soup = BeautifulSoup(html.text, 'html.parser')
    items = soup.find_all('div', class_='post__item grey')
    faculties = []
    for item in items:
        faculties.append(
            {
                'name': item.find('a', class_='link_dark').get_text().replace("\xa0", " "),
                'link': item.find('a', class_='link_dark').get('href')
            }
        )
    return faculties


def get_BM_courses(params=''):
    url = HOST + f'n/education/{degree}/page/{page}/'
    html = get_html(url, params=params)
    soup = BeautifulSoup(html.text, 'html.parser')

    # courses_list = soup.find('div', class_='e-cards__list')
    items = soup.find_all('a', class_='e-card e-cards__item')
    bachelor_courses = []
    links = []

    for link in soup.find_all('a'):
        ref = link.get('href')
        if f'{ref_sign}' in ref:
            links.append(ref)

    course_number = 0
    for item in items:
        places_list = item.find('ul', class_='e-card__label')

        if places_list is not None:
            places_text = ''

            for place in places_list:
                places_text += " " + place.get_text()

            while places_text[0] == ' ':
                places_text = places_text[1:]

            if places_text[-1] == ' ':
                places_text = places_text[:-1]
        else:
            places_text = 'Нет информации'

        course = {
            'name': item.find('div', class_='e-card__category').get_text(),
            'link': links[course_number],
            'language': item.find('p', class_='e-card__label').get_text(),
            'location': item.find('li', class_='e-icon e-card__icon e-icon_pin').get_text(),
            'duration': item.find('li', class_='e-icon e-card__icon e-icon_duration').get_text(),
            'places': places_text,
            'education form': item.find('ul', class_='e-tags e-card__top').get_text()
        }  # upload payment info???

        bachelor_courses.append(course)
        course_number += 1
    return bachelor_courses


def get_fdp_courses(params=''):
    url = HOST + 'n/education/fdp/'
    html = get_html(url, params=params)
    soup = BeautifulSoup(html.text, 'html.parser')
    items = soup.find_all('a', class_='e-card e-cards__item')

    links = []
    for link in soup.find_all('a'):
        ref = link.get('href')
        if 'fdp' in ref:
            links.append(ref)

    course_number = 0
    courses = []
    for item in items:

        price = ''
        for current_price in item.findAll('li', class_='e-card__label'):
            price += current_price.get_text() + '; '
        price = price[:-2]

        course = {
            'name': item.find('span', class_='e-card__title-inner').get_text(),
            'link': links[course_number],
            'description': item.find('div', class_='e-card__description').get_text(),
            'group_form': item.find('li', class_='e-icon e-card__icon e-icon_people').get_text(),
            'duration': item.findAll('p', class_='e-card__label')[1].get_text(),
            'price': price,
            'education_form': item.find('li', class_='e-tag e-tags__item e-color-yellow').get_text()[1:]
        }
        course_number += 1
        courses.append(course)
    return courses


def get_dpo_courses(params=''):
    url = HOST + f'n/education/dpo/page/{page}/'
    html = get_html(url, params=params)
    soup = BeautifulSoup(html.text, 'html.parser')
    items = soup.find_all('a', class_='e-card e-cards__item')

    courses = []
    course_number = 0
    courses_list = soup.find('div', class_='e-cards__list')
    links = []
    for link in courses_list.find_all('a'):
        links.append(link.get('href'))

    for item in items:

        course = {
            'name': item.find('span', class_='e-card__title-inner').text,
            'link': links[course_number]
        }
        courses.append(course)
        course_number += 1
    return courses


if __name__ == '__main__':

    ref_sign = ''; page = 2; degree = ''
    for course in get_dpo_courses(params={'page': page}):
        print(course)

