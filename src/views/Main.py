from flet import Page, Container, Row, VerticalDivider, FilePicker

# from Appbar import Appbar
from .SideMenu import SideMenu
# from .Login import Login
from .Home import Home
# from Users import Users
# from Customers import Customers
# from RegisterCustomer import RegisterCustomer
# from Products import Products
# from RegisterProducts import RegisterProducts
# from Sales import Sales
# from RegisterSales import RegisterSales
# from Config import Config

class Main:
    def __init__(self, page: Page):
        self.page = page
        
        self.menu = SideMenu(self)

        # self.bar = Appbar(self)
        # self.page.navigation_bar = self.bar.build()
    
        """
        creates instances of views and passes the class itself as a parameter
        for all of them, facilitating communication between all classes
        """
        # self.login = Login(self)
        self.home = Home(self)
        # self.users = Users(self)
        # self.customers = Customers(self)
        # self.products = Products(self)

        # # Creates instances of dialogs
        # self.pick_files_dialog = FilePicker()
        # self.save_file_dialog = FilePicker()
        # self.get_directory_dialog = FilePicker()
        # # hide all dialogs in overlay
        # self.page.overlay.extend([self.pick_files_dialog, self.save_file_dialog, self.get_directory_dialog])

        # Creates dict of routes:
        self.routes = {
            "/": self.home,
            "/home": self.home,
            # "/users": self.users,
            # "/customers": self.customers,
            # "/products": self.products
        }
        
        # Creates dict of method to initialize the Views:
        # self.calls = {
        #     "/": self.login.initialize,
        #     "/home": self.home.initialize,
        #     "/users": self.users.initialize,
        #     "/customers": self.customers.initialize,
        #     "/products": self.products.initialize
        # }

        # body:
        self.container = Container(expand=True, content=self.routes["/"])
        self.body = Row(
            expand=True,
            controls=[
                self.menu,
                VerticalDivider(width=1),
                self.container,
            ]
        )
        
        # # Create configs
        # self.config = Config(self)

    def route_change(self, e):
        # Change View:
        self.container.content = self.routes[e.route] 
        #self.body.update()
        self.page.update()

        # Initialize the View
        # self.calls[e.route]()
        
        self.page.update()