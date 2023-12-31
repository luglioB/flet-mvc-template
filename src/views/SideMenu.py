from flet import (UserControl, Container, IconButton, icons, NavigationRail, NavigationRailLabelType,
                  NavigationRailDestination, Icon, padding, border_radius, colors)

from .View import View

class SideMenu(View):
    ext = True
    def __init__(self, route):
        super().__init__()
        self.route = route
        
        self.cont = Container(            
            padding=padding.all(5),
            # bgcolor=colors.ON_INVERSE_SURFACE,                       
            border_radius=border_radius.all(5),
            visible=True,
        )        
        self.nnrail = NavigationRail(
            extended=self.ext,
            label_type=NavigationRailLabelType.NONE,
            min_width=56,                
            min_extended_width=160, 
            bgcolor='transparent',
            leading=IconButton(icon=icons.SWAP_HORIZ_ROUNDED, icon_size=40, tooltip="Show/Hide", on_click=self.menu_clicked),
            group_alignment=-0.95,
            destinations=[
                NavigationRailDestination(
                    icon=icons.COTTAGE_OUTLINED, selected_icon=icons.COTTAGE, label='Home',
                ),
                # NavigationRailDestination(
                #     icon_content=Icon(icons.PERM_CONTACT_CALENDAR_OUTLINED), selected_icon_content=Icon(icons.PERM_CONTACT_CALENDAR), label='Customers'
                # ),
                # NavigationRailDestination(
                #     icon_content=Icon(icons.PERSON_OUTLINED), selected_icon_content=Icon(icons.PERSON_ROUNDED), label='Users'
                # ),
                # NavigationRailDestination(
                #     icon_content=Icon(icons.INVENTORY_2_OUTLINED), selected_icon_content=Icon(icons.INVENTORY), label='Products'
                # ),
                # NavigationRailDestination(
                #     icon_content=Icon(icons.SHOPPING_CART_OUTLINED), selected_icon_content=Icon(icons.SHOPPING_CART), label='Sales'
                # ),
                # NavigationRailDestination(
                #     icon=icons.SETTINGS_OUTLINED, selected_icon_content=Icon(icons.SETTINGS), label='Configurações',
                # ),
            ],
            on_change=self.nav_clicked,
        )  
        self.cont.content=self.nnrail

    def build(self):
        return self.cont

    def menu_clicked(self, e):
        self.nnrail.extended = not self.nnrail.extended        
        self.ext = self.nnrail.extended
        self.update()

    def nav_clicked(self, e):
        index = e.control.selected_index
        print(f"selected {index}")
        if e.control.selected_index == 0:            
            self.page.go("/home")
            # self.route.bar.set_title('Home')
            self.route.page.update()
            self.update()
            return
        # elif e.control.selected_index == 1:
        #     self.page.go("/customers")
        #     self.route.bar.set_title('Customers')
        #     self.route.page.update()
        #     self.update()
        #     return
        # elif e.control.selected_index == 2:            
        #     self.page.go("/users")
        #     self.route.bar.set_title('Users')
        #     self.route.page.update()
        #     self.update()
        #     return
        # elif e.control.selected_index == 3:            
        #     self.page.go("/products")
        #     self.route.bar.set_title('Products')
        #     self.route.page.update()
        #     self.update()
        #     return
