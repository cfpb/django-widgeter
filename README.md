[![Build Status](https://travis-ci.org/dlapiduz/django-widgeter.png?branch=master)](https://travis-ci.org/dlapiduz/django-widgeter)

Widgeter
========================

A simple engine for django backend widgets.

Widgets are snippets of code that render into a template. They can be used when you need to include a template with
a context that is not available in the front end.

Moreover, widgets can be added by reusable apps without the need for the main project to know what their requirements are.


Features
-----------------

- Creation of custom widgets in reusable apps
- Rendering of widgets by name
- Rendering of widget blocks without previous knowledge of widget names
- Autodiscovery of widgets from all installed apps


Installation
-----------------

1. Install the package using `pip install django-widgeter`
1. Add `widgeter` to your `INSTALLED_APPS` in `settings.py`


Defining a Widget
-----------------

Add a `widgets.py` file on your application with the following statements.

- Widgets can be defined with a template (and optionally a context):
  ```
    from widgeter.core import Widget
    
    class HelloWorld(Widget):
        template = 'hello_world/widget.html'

        def get_context(self, context, options=None):
            return { 'message': u'Hello World!' }
  ```

  or with a render function:
  ```
    from widgeter.core import Widget
    
    class HelloWorld(Widget):
        def render(self, context, options=None):
            return u'Hello world!'

  ```
- Register your widget:
  ```
    from widgeter.registry import registry

    registry.register('hello_world', HelloWorld())
  ```


Rendering a Widget
-----------------

On a template you first have to load the template tags and then render the particular widget:

```
  {% load widgeter %}
  {% widget "hello_world" %}
```

You can also pass variables to your widget:

```
  {% load widgeter %}
  {% widget "hello_world" current_user %}
```


Using Blocks
-----------------

Widget blocks allow you to render widgets without previously knowing the names for them.
The autodiscovery process will add them to the registry and you can the look them up by block name.
Priorities can also be assigned to render them in order.

- First define a block on the widget:
  ```
    from widgeter.core import Widget
    
    class HelloWorld(Widget):
        block = 'home'
        priority = '1'
        template = 'hello_world/widget.html'

        def get_context(self, context, options=None):
            return { 'message': u'Hello World!' }
  ```

- Then, on the template, use the `widget_block` tag:
  ```
    {% load widgeter %}
    {% widget_block "home" current_user %}
  ```

Running the Tests
------------------------------------

You can run the tests with via::

    python setup.py test

or::

    python runtests.py


Inspiration
--------------
This project is based on https://github.com/marcinn/django-widgets but updated for new versions of Django.
