import flet as ft 


def LoginPage(e, page : ft.Page):

    page.clean()
    
    page.appbar = ft.AppBar(
        bgcolor=ft.colors.TRANSPARENT,
        leading=ft.IconButton(
            icon=ft.icons.ARROW_BACK_IOS_NEW,
            on_click=lambda _,page=page:IndexPage(page)
        )
    )
    
    username_field = ft.TextField(
        width= 300,
        label="Username",
        bgcolor=ft.colors.WHITE   
    )
    
    password_field = ft.TextField(
        width= 300,
        label="Password",
        bgcolor=ft.colors.WHITE   
    )
    
    page.add(
        ft.Image(src="index_image.png", width=150, height=150),
        
        username_field,
        
        password_field,
        
        ft.ElevatedButton("Login", width=300, on_click=lambda _: print("hah"))
        
    )


def SignUpPage(e, page : ft.Page):
    
    page.clean()
    
    page.appbar = ft.AppBar(
        bgcolor=ft.colors.TRANSPARENT,
        leading=ft.IconButton(
            icon=ft.icons.ARROW_BACK_IOS_NEW,
            on_click=lambda _,page=page:IndexPage(page)
        )
    )
    
    
    username_field = ft.TextField(
        width= 300,
        label="Username",
        bgcolor=ft.colors.WHITE   
    )
    email = ft.TextField(
        width= 300,
        label="Email",
        bgcolor=ft.colors.WHITE   
    )
    
    password_field = ft.TextField(
        width= 300,
        label="Password",
        bgcolor=ft.colors.WHITE,
        can_reveal_password=True,
        password=True
    )
    
    page.add(
        ft.Image(src="index_image.png", width=150, height=150),
        
        username_field,
        
        email
        ,
        
        password_field,
        
        ft.ElevatedButton("Sign Up", bgcolor=ft.colors.GREEN,color=ft.colors.WHITE,width=300, on_click=lambda _: print("hah"))
        
    )


def IndexPage(page : ft.Page):
    
    page.clean()
    
    page.appbar = None
    
    
    page.add(
        ft.Image(src="index_image.png", width=150, height=150)
        ,
        ft.Text("AskSecert", color=ft.colors.WHITE),
        
        ft.ElevatedButton("Login", on_click=lambda e,page=page:LoginPage(e,page)),
        
        ft.ElevatedButton("Sign Up",on_click=lambda e,page=page : SignUpPage(e, page))
    )
