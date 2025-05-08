import reflex as rx
from PomodoroStudy.state import State
from PomodoroStudy.ui.base import base_page




def settings_page() -> rx.Component:
    # settings Page
    my_child =  rx.vstack(
            rx.heading(State.label_settings, size="9"),
            rx.text(
                "edit your settings",
                size="5",
            ),
             
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id="my-child"
        )
    return base_page(my_child)