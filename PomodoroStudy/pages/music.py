import reflex as rx
from PomodoroStudy.state import State
from PomodoroStudy.ui.base import base_page



def music_page() -> rx.Component:
    # music Page
    my_child =  rx.vstack(
            rx.heading(State.label_music, size="9"),
            rx.text(
                "Pick the music you like",
                size="5",
            ),
             
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id="my-child"
        )
    return base_page(my_child)