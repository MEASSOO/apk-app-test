import flet as ft
from pages.index import IndexPage


def main(page: ft.Page):
    
    
    page.title = 'App'
    page.bgcolor = ft.colors.BLUE_GREY_500
    page.window.height = 560
    page.window.width = 360
    # page.appbar = ft.AppBar(
    #     leading=ft.Text("Text"),
    #     center_title=True
    # )
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    
    def change_route(route):
        troute = ft.TemplateRoute(page.route)
        
        if troute.match("/"):
            
            IndexPage(page)
            
        

        
    
    # page.add()

    page.on_route_change = change_route
    
    page.go("/")

ft.app(main)
