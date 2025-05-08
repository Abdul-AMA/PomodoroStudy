"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from PomodoroStudy.ui.base import base_page
from rxconfig import config


class State(rx.State):
    """The app state."""
    label2 = "watch for the button"

    def handle_input_change(self,val):
        self.label2 = val



def index() -> rx.Component:
    # Welcome Page (Index)
    return base_page(
        rx.vstack(
            rx.heading(State.label2, size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.input(
                default_value="Write your name",
                on_change=State.handle_input_change
                ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
     )


app = rx.App()
app.add_page(index)
