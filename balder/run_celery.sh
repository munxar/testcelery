export DJANGO_SETTINGS_MODULE=balder.settings
celery -A async.celery_app worker --loglevel=info
