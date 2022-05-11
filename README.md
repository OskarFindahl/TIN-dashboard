# TIN Dashboard

## REST API Documentation.
You must run backend server to access api documentation.
Follow steps in [backend setup](#backend).
Documentation for API can then be found in read-able format at `http://localhost:8000/swagger/`.
And in open-api format on: `http://localhost:8000/swagger/?format=openapi`

## Setup guide

### Backend {#backend}
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
Seed database with mock data.
```
py manage.py loaddata data.json
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