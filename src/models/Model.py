class Model:

    def __init__(self):
        self._views = []

    def subscribe(self, view):
        self._views.append(view)

    def notify_views(self, *args, **kwargs):
        for view in self._views:
            view.on_state_changed(*args, **kwargs)

    def unsubscribe(self, observer):
        self._views.remove(observer)