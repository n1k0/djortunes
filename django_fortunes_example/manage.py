#!/usr/bin/env python
import os, site, sys

from django.core.management import execute_manager
from django.core.management import setup_environ

ROOT = os.path.dirname(os.path.abspath(__file__))
path = lambda *a: os.path.join(ROOT, *a)

site.addsitedir(path('apps'))
site.addsitedir(path('lib'))

try:
    import settings
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

setup_environ(settings)

if __name__ == "__main__":
    execute_manager(settings)