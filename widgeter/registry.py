class WidgetRegistry():
    widgets = {}

    def register(self, name, widget):
        """Register a widget in the registry under a given name"""
        if self.widgets.has_key(name):
            raise KeyError('Widget "%s" is already registered' % name)

        self.widgets[name] = widget

    def get(self, name):
        """Get a widget by name from the registry"""
        return self.widgets[name]

    def get_by_block(self, block_name):
        """Get all the widgets from a given block"""
        return [self.widgets[i] for i in self.widgets if self.widgets[i].block == block_name]

registry = WidgetRegistry()
