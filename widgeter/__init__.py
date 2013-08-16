"Widgeter: A simple engine for backend widgets"

__version__ = '0.0.1'

from django.conf import settings


def autodiscover():
    for app in settings.INSTALLED_APPS:
        __import__(app, {}, {}, ['widgets'])

autodiscover()
