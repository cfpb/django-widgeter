from django.test import TestCase
from widgeter.registry import registry
from widgeter.core import Widget
from django.template import Template, Context, TemplateSyntaxError


class RegistryTest(TestCase):
    def setUp(self):
        registry.widgets = {}

    def test_register_valid(self):
        widget = 'widget'
        registry.register('widget', widget)
        self.assertIn(widget, registry.widgets)
        self.assertEqual(widget, registry.get('widget'))

    def test_register_dup(self):
        widget = 'widget'
        registry.register('widget', widget)
        with self.assertRaises(KeyError):
            registry.register('widget', widget)

    def test_get_by_block(self):
        class Test1(Widget):
            block = 'testing'
        test1 = Test1()
        registry.register('test1', test1)

        class Test2(Widget):
            block = 'not_testing'
        test2 = Test2()
        registry.register('test2', test2)

        class Test3(Widget):
            block = 'testing'
        test3 = Test3()
        registry.register('test3', test3)

        widgets = registry.get_by_block('testing')

        self.assertIn(test1, widgets)
        self.assertNotIn(test2, widgets)
        self.assertIn(test3, widgets)


class TemplateTagTest(TestCase):
    def setUp(self):
        registry.widgets = {}

    def test_widget(self):
        class HelloWorld(Widget):
            def render(self, context, options):
                return u'Hello world!'

        registry.register('helloworld', HelloWorld())

        out = Template(
            "{% load widgeter %}"
            "{% widget \"helloworld\" %}"
            ).render(Context())
        
        self.assertIn('Hello world!', out)

    def test_widget_block(self):
        class HelloWorld(Widget):
            block = "testing"
            def render(self, context, options):
                return u'Hello world!'

        registry.register('helloworld', HelloWorld())

        class FooBar(Widget):
            block = "not_testing"
            def render(self, context, options):
                return u'Bye bye world!'

        registry.register('foobar', FooBar())


        out = Template(
            "{% load widgeter %}"
            "{% widget_block \"testing\" %}"
            ).render(Context())
        
        self.assertIn('Hello world!', out)
        self.assertNotIn('Bye bye world!', out)


