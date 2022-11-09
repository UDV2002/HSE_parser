from dataclasses import dataclass
from enum import Enum
import parser
import click, typer


class Campus(Enum):
    Moscow = 'Москва'
    Novgorod = 'Нижний Новгород'
    Petersburg = 'Санкт-Петербург'
    Perm = 'Пермь'


@dataclass
class Faculty:
    name: str = ''; link: str = ''

    def set_all(self, name, link):
        self.name = name
        self.link = link

    def print_values(self):
        print(f'Название факультета: {self.name}\n'
              f'Ссылка: {self.link}\n\n')


@dataclass
class Course:
    name: str = ''; link: str = ''; language: str = '';
    location: str = ''; duration: str = ''
    places: str = ''; education_form: str = ''

    def set_all(self, params):
        self.name = params.get('name'); self.link = params.get('link')
        self.language = params.get('language'); self.location = params.get('location')
        self.duration = params.get('duration'); self.places = params.get('places')
        self.education_form = params.get('education form')

    def print_values(self):
        message = f'Название курса: {self.name}\n' \
                  f'Ссылка: {self.link}\n' \
                  f'Язык курса: {self.language}\n' \
                  f'Кампус: {self.location}\n' \
                  f'Продолжительность курса: {self.duration}\n' \
                  f'Квоты на обучение: {self.places}\n' \
                  f'Форма обучения: {self.education_form}\n\n'
        print(message)


if __name__ == '__main__':
    print('classes.py')


