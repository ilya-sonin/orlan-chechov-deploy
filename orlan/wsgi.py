import os
import sys

sys.path.append('/home/c/ck09478/orlan_django_wagtail/public_html/')
sys.path.append('/home/c/ck09478/myenv/lib/python3.4/site-packages/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'orlan.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()