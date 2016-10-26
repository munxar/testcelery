* INSTALL *
inside of testcelery execute:
- virtualenv --no-site-packages venv
- source venv/bin/active
- pip install -r requirements.txt
- cd balder
- ./manage.py migrate
- ./manage.py createsuperuser

* RUN *
- source venv/bin/active
- cd balder

to run webui
- ./manage.py runserver
- browse to http://127.0.0.1:8000/admin and login

to run celery worker
- ./run_celery
