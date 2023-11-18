from flet import Page, app, Theme, ThemeMode, colors

# from views.Main import Main
from models.User import User
from controllers.UserController import UserController
from views.View import View
from views.Main import Main

# def main(page: Page):
#     page.title='Infostore'
#     page.window_min_height = 700
#     page.window_min_width = 1360

#     page.theme_mode=ThemeMode.LIGHT
#     page.theme = Theme(color_scheme_seed=colors.BLUE_300)

#     _app = Main(page)
#     page.on_route_change = _app.route_change    

#     page.add(
#         _app.body
#     )
    
#     page.go("/")
#     page.update()

def main(page: Page):
    page.title='MyApp'
    page.window_min_height = 700
    page.window_min_width = 1360

    page.theme_mode=ThemeMode.LIGHT
    page.theme = Theme(color_scheme_seed=colors.BLUE_300)

    user_model = User()
    user_controller = UserController(user_model)

    _app = Main(page)
    page.on_route_change = _app.route_change    

    page.add(
        _app.body
    )
    
    page.go("/")
    page.update() 

if __name__ == "__main__":
    app(target=main)