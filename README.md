
# HSE_parser

Проект для сохранения и использования данных с сайта https://www.hse.ru 
## Системные требования:
* Python 3.6+
* PostgreSQL 15+
# Установка:
## Установленные пакеты python:
psycopg2, bs4, typer, requests - устанавливаются командной в терминале python либо в командной строке в соответствующей директории
```
pip install psycopg2, bs4, typer, requests
```

## База данных

Для работы проекта нужна база данных. В папке проекта лежит архив HSE_dump.zip. Посе его распаковки и сохранения файла HSE.dump в командной строке следует воспользоваться следующей командой с заменой аргументов на соответствующие (username, dbname, filename):

```bash
  pg_restore -U username -d dbname -1 filename.dump
```
Команда должна восстановить базу данных со всеми актуальными данными. 
Либо можно воспользоваться функцией Restore в менеджере баз данных PgAdmin, чтобы выбрать dump файл.

# Как пользоваться
## Команды для командной строки Windows
Перед использованием команд, нужно перейти в соответствующую директорию:

```
cd *path_to_project
```
path_to_project - Полный путь до файла main.py в проекте 
### Получить списки факультетов

```
  python main.py show-faculties {Parameter}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `all` | `string` | Выводит всю информацию по факультетам |
| `names` | `string` | Выводит названия факультетов |
| `links` | `string` | Выводит ссылки на веб-страницы факультетов |

Параметры вводятся в любом порядке через дефис "-". Пример использования ниже:
```
  python main.py show-faculties names-links # Выведет названия и ссылки
  python main.py show-faculties all         # Выведет всю информацию по факультетам 
```
### Получить списки курсов бакалавриата

```
  python main.py show-bachelor-courses {Parameter}
```


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | Выводит всю информацию по факультетам |
| `names` | `string` | Выводит названия факультетов |
| `links` | `string` | Выводит ссылки на веб-страницы факультетов |
| `educationforms` | `string` | Выводит формы обучения (очная/заочная) |
| `durations` | `string` | Выводит продолжительность курса обучения |
| `places` | `string` | Выводит квоты на курс |
| `languages` | `string` | Выводит языки, на котором идет преподавание |
| `campuses` | `string` | Выводит город компуса (Москва, Петербург и т.д.) |

Параметры вводятся в любом порядке через дефис "-". Пример использования ниже:
```
  python main.py show-bachelor-courses names-durations # Выведет названия и продолжительность обучения
  python main.py show-bachelor-courses all             # Выведет всю информацию по курсам 
```

### Получить списки курсов магистратуры

```
  python main.py show-magister-courses {Parameter}
```


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | Выводит всю информацию по факультетам |
| `names` | `string` | Выводит названия факультетов |
| `links` | `string` | Выводит ссылки на веб-страницы факультетов |
| `educationforms` | `string` | Выводит формы обучения (очная/заочная) |
| `durations` | `string` | Выводит продолжительность курса обучения |
| `places` | `string` | Выводит квоты на курс |
| `languages` | `string` | Выводит языки, на котором идет преподавание |
| `campuses` | `string` | Выводит город компуса (Москва, Петербург и т.д.) |

Параметры вводятся в любом порядке через дефис "-". Пример использования ниже:
```
  python main.py show-magister-courses names-durations # Выведет названия и продолжительность обучения
  python main.py show-magister-courses all             # Выведет всю информацию по курсам 
```


## Файлы проекта

```
parser.py -
    скрипт с функциями для получения информации с сайта ВШЭ
db_manager.py -
    скрипт с функциями для создания таблиц, заполнения их данными, полученными с сайта
classes.py -
    содержит классы для упрощения сохранения информации и более удобной работы с ней
db_config.py -
    файл с конфигурациями, необходимыми для подключения к базе данных
parsing_sources.txt -
    файл с перечислением веб страниц и кратким описанием полезной информации, расположенной на них
main.py -
    скрипт с функциями и командами для получения данных из бд через командную строку:
Backup.cmd -
    скрипт для создания бэкапа базы данных
HSE_dump.zip -
    архив с файлом Restore.cmd
Restore.cmd -
    скрипт для восстановления базы данных
```

