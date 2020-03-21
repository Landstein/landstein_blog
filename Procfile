/* web: gunicorn eric.wsgi --log-file - */
web: python manage.py collectstatic --no-input; gunicorn eric.wsgi --log-file - --log-level debug
