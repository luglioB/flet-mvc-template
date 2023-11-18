import flet as ft

class Home(ft.UserControl):
    def __init__(self, route):
        super().__init__()
        self.route = route

    def build(self):
        return ft.Container(
            content=ft.Row(
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Home is working")
                ]
            ),
            expand=True,
            alignment=ft.alignment.center,            
        )