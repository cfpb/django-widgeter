from django.conf import settings


def autodiscover():
    """Find all the widgets within the installed apps""" 
    for app in settings.INSTALLED_APPS:
        __import__(app, {}, {}, ['widgets'])

autodiscover()
