import reflex as rx

from PomodoroStudy.ui import side

def base_page(child : rx.Component,*args,**kwargs) -> rx.Component :
    return rx.fragment(
        side.sidebar_bottom_profile(),
        rx.box(
            child,
        ),
        rx.logo(),    
    )

