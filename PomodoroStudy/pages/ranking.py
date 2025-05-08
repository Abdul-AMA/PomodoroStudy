import reflex as rx
from PomodoroStudy.state import State
from PomodoroStudy.ui.base import base_page



def ranking_page() -> rx.Component:
    # ranking Page
    my_child =  rx.vstack(
            rx.heading(State.label_ranking, size="9"),
            rx.text(
                "this is your rank",
                size="5",
            ),
             
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id="my-child"
        )
    return base_page(my_child)