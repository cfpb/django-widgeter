from django.conf import settings


def autodiscover():
    for app in settings.INSTALLED_APPS:
        __import__(app, {}, {}, ['widgets'])

autodiscover()
