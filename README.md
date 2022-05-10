# TIN Dashboard

## Setup guide

### Backend
```
cd backend
```
Create virtual environment.
```
py -m venv venv
```
Activate virtual environment.

Install dependencies.
```
pip install -r requirements.txt
```
Apply migrations
```
py manage.py migrate
```
Run server
```
py manage.py runserver
```

### Scraper
> Can only run with api-key. Set in local_settings.py
```
cd scraper
```
Create virtual environment.
```
py -m venv venv
```
Activate virtual environment.

Install dependencies.
```
pip install -r requirements.txt
```
Run spider
```
scrapy crawl zyte_spider
```

### Frontend
```
cd frontend
```

Install dependencies.
```
npm i
```
Run server
```
npm run dev
```