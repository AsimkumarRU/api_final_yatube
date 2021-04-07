# API Yatube
REST API для социальной сети блогеров [Yatube](https://github.com/AsimkumarRU/hw05_final).
## Функции
* аутентификация по JWT-токену
* работа со всеми модулями социальной сети Yatube: постами, комментариями, группами, подписчиками
* поддержка методов GET, POST, PUT, PATCH, DELETE
* предоставление данных в формате JSON
## Установка
1. Клонируем репозиторий с проектом себе на компьютер
```python
$ git clone https://github.com/AsimkumarRU/api_final_yatube
```
2. Создаем виртуальное окружение
```python
$ python -m venv venv
```
3. Устанавливаем зависимости
```python
$ pip install -r requirements.txt
```
4. Создаем и применяем миграции
```python
$ python manage.py makemigrations
$ python manage.py migrate
```
5. Запускаем django сервер
```python
$ python manage.py runserver
```
Все готово к использованию API.
## Аутентификация
Выполните POST-запрос localhost:8000/api/v1/token/, передав поля username и password.
API вернет JWT-токен в формате:
```
{
    "refresh": "ХХХХХХХХХХХ",
    "access": "ХХХХХХХХХХХХ"
}
```
