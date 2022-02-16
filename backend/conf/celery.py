from __future__ import absolute_import, unicode_literals
import os
import celery
from django.conf import settings
# from dotenv import load_dotenv
# load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "conf.settings")

app = celery.Celery('conf', config_source=settings.CELERY)
app.autodiscover_tasks()
