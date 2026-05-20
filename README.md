# Habit Tracker API (DRF + Docker + CI/CD)

## Описание

Сервис для отслеживания полезных привычек с интеграцией уведомлений в Telegram.

## Технологии

* Python 3.12 / Django / DRF

* PostgreSQL — основная база данных

* Redis + Celery — фоновые задачи (уведомления)

* Nginx — веб-сервер (reverse proxy)

* Docker / Docker Compose — контейнеризация

* GitHub Actions — автоматический линтинг, тесты и деплой

## Запуск проекта локально

1. Клонировать репозиторий.

```
git clone https://github.com/kpas955/Course_DRF.git
cd Course_DRF
```

2. Создайте файл .env в корне проекта и заполните его по образцу:

```
SECRET_KEY =django-insecure...

# Токен вашего бота от @BotFather
TELEGRAM_BOT_TOKEN=ваш_токен

# Ваш Telegram ID (можно узнать у @userinfobot)
TELEGRAM_CHAT_ID=ваш_id

DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=ваш_пароль
DB_HOST=db
DB_PORT=5432

CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0

DEBUG=False
```

3. Запустите проект:

```
docker compose up -d --build
```

Проект будет доступен по адресу: http://localhost/

## Настройка CI/CD и деплоя

Проект настроен на автоматический деплой при пуше в ветку home_work.
Настройка GitHub Secrets

Для работы Pipeline необходимо добавить следующие секреты в настройках репозитория (Settings -> Secrets -> Actions):

* SSH_HOST — IP-адрес вашего сервера.

* SSH_USER — имя пользователя (например, kottt95).

* SSH_KEY — приватный SSH-ключ для доступа к серверу.

* DB_PASSWORD — пароль от базы данных для прохождения тестов.

* SECRET_KEY — django-insecure...

## Этапы Pipeline:

1. Linting: Проверка кода через flake8.
2. Testing: Запуск тестов через pytest.
3. Deploy: При успешных тестах — подключение к серверу через SSH, git pull и перезапуск контейнеров через docker compose
   up -d --build.

## Документация API

После запуска документация доступна по адресам:

* Swagger: http://81.26.190.237/api/docs/

* Redoc: http://81.26.190.237/api/schema/