from django.template import Library, Node, TemplateSyntaxError, Variable
from ..registry import registry

register = Library()


class WidgetNode(Node):
    """Django template node to render a single widget"""
    def __init__(self, name, opt_var):
        self.name = name
        self.opt_var = opt_var

    def render(self, context):
        if self.opt_var:
            self.opt_var = Variable(self.opt_var).resolve(context)
        return registry.get(self.name).render(context, self.opt_var)


@register.tag(name='widget')
def widget(parser, token):
    """Render a single widget by name"""
    opts = token.split_contents()
    if len(opts) < 2:
        raise template.TemplateSyntaxError("%r tag requires at least one argument" % token.contents.split()[0])
    tag_name = opts[0]
    name = opts[1]
    if not (name[0] == name[-1] and name[0] in ('"', "'")):
        raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)
    try:
        opt_var = opts[2]
    except:
        opt_var = None
    return WidgetNode(name[1:-1], opt_var)


class WidgetBlockNode(Node):
    """Django template node to render a widget block"""
    def __init__(self, name, opt_var):
        self.name = name
        self.opt_var = opt_var

    def render(self, context):
        if self.opt_var:
            self.opt_var = Variable(self.opt_var).resolve(context)
        widgets = registry.get_by_block(self.name)
        output = ""
        for widget in widgets:
            output += widget.render(context, self.opt_var)

        return output


@register.tag(name='widget_block')
def widget_block(parser, token):
    """Render all the widgets in a given block"""
    opts = token.split_contents()
    if len(opts) < 2:
        raise template.TemplateSyntaxError("%r tag requires at least one argument" % token.contents.split()[0])
    tag_name = opts[0]
    name = opts[1]
    if not (name[0] == name[-1] and name[0] in ('"', "'")):
        raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)
    try:
        opt_var = opts[2]
    except:
        opt_var = None
    return WidgetBlockNode(name[1:-1], opt_var)
