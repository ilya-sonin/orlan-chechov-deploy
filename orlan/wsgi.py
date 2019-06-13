import os
import sys

sys.path.append('/home/c/ck09478/orlan_django_wagtail/public_html/')
sys.path.append('/home/c/ck09478/orlan_django_wagtail/public_html/myenv/lib/python3.4/site-packages/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'orlan.settings'

import django
django.setup()

from django.core.handlers import wsgi
application = wsgi.WSGIHandler()