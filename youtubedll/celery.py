from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youtubedll.settings')
app = Celery('youtubedll')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
