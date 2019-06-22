# 🚀 Space flights management system 🚀

clone the project

`git clone https://github.com/tylluan/space-flights.git`

create and start a a virtual environment

`virtualenv env --no-site-packages`

`source env/bin/activate`

Install the project dependencies:

`pip3 install -r requirements.txt`

create a file named ".env"

`mkdir static  && touch static/.env` (mac and linux)
`mkdir static && type nul > static/.env` (windows)

obtain a secret from MiniWebTool key and add to .env

- linux and mac:
```bash 
echo 'SECRET_KEY="<secret_key>"
PASSWORD = "<password>"' > static/.env
``` 
- widows

```(echo SECRET_KEY="<secret_key>" & echo PASSWORD = "<password>") > static/.env```

add .env to .gitignore file

create a postgres db and add the credentials to settings.py

```python
DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'name',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

then run

`python manage.py migrate`

create admin account

`python manage.py createsuperuser`

then make migrations for the app:

`python manage.py makemigrations`

migrate them:

`python manage.py migrate`

and start the development server:

`python manage.py runserver`

and open `localhost:8000` on your browser to view the app.
