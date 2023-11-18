from flet import UserControl
from models.Model import Model

class View(UserControl):

    def __init__(self, model: Model=None, controller=None):
        super().__init__()
        self.model = model
        self.controller = controller
        if self.model:
            self.model.subscribe(self)

    def on_state_changed(
        self,
        *args,
        **kwargs
        ):
        print ('Got', args, kwargs, 'From', self.model)