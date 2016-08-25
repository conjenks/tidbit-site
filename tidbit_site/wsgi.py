import os
import sys
sys.path.append('C:/djangostack-1.9.8-0/apps/django/django_projects/tidbit_site')
os.environ.setdefault("PYTHON_EGG_CACHE", "C:\Users\Administrator\AppData\Roaming\Python-Eggs")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tidbit_site.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()