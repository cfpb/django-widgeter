class WidgetRegistry():
    widgets = {}

    def register(self, name, widget):
        if self.widgets.has_key(name):
            raise KeyError('Widget "%s" is already registered' % name)

        self.widgets[name] = widget

    def get(self, name):
        return self.widgets[name]

    def get_by_channel(self, channel_name):
        return [self.widgets[i] for i in self.widgets if self.widgets[i].channel == channel_name]

registry = WidgetRegistry()
