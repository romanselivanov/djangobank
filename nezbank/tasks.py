from conf.celery import app
from django.core.management import call_command


@app.task
def check_currency(*args):
    call_command('check_currency', verbosity=0)
