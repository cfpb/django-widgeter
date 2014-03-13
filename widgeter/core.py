from registry import registry
from django.template.loader import get_template


class Widget():
    """Core class for widgeter. All widgets will extend this class."""
    template = None
    block = None
    priority = 100

    def __init__(self, *args, **kwargs):
        self.template_instance = None


    def get_context(self, value, options):
        """This function can be patched in any widget to add variables to the context"""
        return {}

    def render(self, context, options=None):
        """
        This is the method that is called to actually render the widget.
        The `template` variable can be set to a file path,
        `template_instance` to a loaded instance of a template,
        or the whole method can be patched to return something else.
        """
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
