"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from PomodoroStudy import pages
from PomodoroStudy.state import State
from PomodoroStudy.ui.base import base_page
from rxconfig import config




def index() -> rx.Component:
    # Welcome Page (Index)

    my_child =  rx.vstack(
            rx.heading(State.label, size="9"),
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
            align="center",
            min_height="85vh",
            id="my-child"
        )
    return base_page(my_child)







app = rx.App()
app.add_page(index)
app.add_page(pages.study_page, route='/study')
app.add_page(pages.music_page, route='/music')
app.add_page(pages.analytics_page, route='/analytics')
app.add_page(pages.ranking_page, route='/ranking')
app.add_page(pages.settings_page, route='/settings')
