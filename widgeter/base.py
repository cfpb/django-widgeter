from registry import registry
from django.template.loader import get_template


class Widget():
    template = None
    channel = None
    priority = 100

    def __init__(self, *args, **kwargs):
        self.template_instance = None


    def get_context(self, value, options):
        return {}

    def render(self, context, options=None):
        if not self.template_instance:
            if not self.template:
                raise RuntimeError('Abstract method Widget.render()\
                        is not implemented')
            self.template_instance = get_template(self.template)

        context.push()
        context.update(self.get_context(context, options))
        result = self.template_instance.render(context)
        context.pop()
        return result
