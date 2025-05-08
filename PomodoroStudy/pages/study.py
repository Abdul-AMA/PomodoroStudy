import reflex as rx
from PomodoroStudy.state import State
from PomodoroStudy.ui.base import base_page




def study_page() -> rx.Component:
    # Study Page
    my_child =  rx.vstack(
            rx.heading(State.label_study, size="9"),
            rx.text(
                "Pick a timer or customize a one",
                size="5",
            ),
             
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id="my-child"
        )
    return base_page(my_child)