# API Yatube

REST API для социальной сети **Yatube**. Позволяет публиковать посты, комментировать их, объединяться в сообщества и подписываться на других авторов.

## Описание

Проект реализован на **Django** и **Django REST Framework**. Аутентификация — по **JWT** (библиотека Djoser). Документация API доступна в формате ReDoc после запуска сервера.

Основные возможности:

- просмотр и создание постов (с изображением и привязкой к сообществу);
- комментарии к постам;
- просмотр сообществ (создание — только через админку);
- подписки на авторов с поиском по имени пользователя.

## Установка

Клонируйте репозиторий и перейдите в каталог проекта:

```bash
git clone <url-репозитория>
cd api-final-yatube-ad
```

Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

Установите зависимости и выполните миграции:

```bash
pip install -r requirements.txt
cd yatube_api
python manage.py migrate
```

Запустите сервер разработки:

```bash
python manage.py runserver
```

Документация API: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

## Примеры запросов

### Получение JWT-токена

```http
POST /api/v1/jwt/create/
Content-Type: application/json

{
  "username": "TestUser",
  "password": "1234567"
}
```

### Список постов

```http
GET /api/v1/posts/
```

### Создание поста (с токеном)

```http
POST /api/v1/posts/
Authorization: Bearer <access-токен>
Content-Type: application/json

{
  "text": "Новый пост"
}
```

### Подписка на автора

```http
POST /api/v1/follow/
Authorization: Bearer <access-токен>
Content-Type: application/json

{
  "following": "username_автора"
}
```

### Список своих подписок с поиском

```http
GET /api/v1/follow/?search=username
Authorization: Bearer <access-токен>
```

Коллекция запросов для **Postman** лежит в каталоге `postman_collection/`.
