# Django Awesome Blog - Michal Durik and Manuel Canzian

This web-application and database are for Modul 133

---

## Requirements

- autopep8==1.4.4
- dj-database-url==0.5.0
- Django==2.2.5
- django-appconf==1.0.3
- django-compressor==2.3
- django-crispy-forms==1.7.2
- django-heroku==0.3.1
- django-libsass==0.7
- django-sass-processor==0.7.3
- gunicorn==19.9.0
- libsass==0.19.2
- pep8==1.7.1
- Pillow==6.1.0
- psycopg2==2.7.5
- pycodestyle==2.5.0
- pytz==2019.2
- rcssmin==1.0.6
- rjsmin==1.1.0
- six==1.12.0
- sqlparse==0.3.0
- whitenoise==4.1.4

---

### Structure

Below, you see the application structure for Awesome Blog.

```
.
├── Procfile
├── README.md
├── blog
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── models.py
│   ├── static
│   │   └── blog
│   │       └── style.css
│   ├── templates
│   │   └── blog
│   │       ├── base.html
│   │       ├── contact.html
│   │       ├── home.html
│   │       ├── impressum.html
│   │       ├── post_confirm_delete.html
│   │       ├── post_detail.html
│   │       ├── post_form.html
│   │       └── robots.txt
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── django_blog
│   ├── __init__.py
│   ├── __pycache__
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── media
│   ├── default.jpg
│   └── profile_pics
│       ├── miko866_-_2.jpg
│       └── miko866_-_2_pD8hk5g.jpg
├── requirements.txt
├── staticfiles
└── users
    ├── __init__.py
    ├── __pycache__
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── __init__.py
    │   └── __pycache__
    ├── models.py
    ├── signals.py
    ├── templates
    │   └── users
    │       ├── login.html
    │       ├── logout.html
    │       ├── profile.html
    │       └── register.html
    ├── tests.py
    └── views.py
```

---

## App Start - Terminal

Create python virtual environment.

### In app root folder.

Start python virtual environment:

```
source myenv/bin/activate
```

Start Django server:

- cd django-blog

```
python manage.py runserver
```

---

## Usage

After you have done the installation you can call the application as follows. For further details see documentation.

### API

- Development: `http://127.0.0.1:8000/`
- Heroku: https://stormy-wave-31811.herokuapp.com/

---

## Copyright

&copy; Michal Durik && Emanuel Canzian <br />
[mdurik2@gmail.com](mailto:mdurik2@gmail.com)<br />
