
import reflex as rx
from PomodoroStudy.state import State
from PomodoroStudy.ui.base import base_page
import assets


def analytics_page() -> rx.Component:
    # analytics Page
    my_child =  rx.vstack(
            rx.heading(State.label_analytics, size="9"),
            rx.text(
                "this is your analytics",
                size="5",
            ),
             
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id="my-child"
        )
    return base_page(my_child)