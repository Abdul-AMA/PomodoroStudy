"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from PomodoroStudy import pages
from PomodoroStudy.state import State
from PomodoroStudy.ui.base import base_page
from rxconfig import config




def index() -> rx.Component:
    # Welcome Page (Index)

    my_child = rx.vstack(
        rx.image(
            src="/logo.png",
            alt="Pomodoro Logo",
            width="100px",
            height="100px"
        ),
        rx.heading("Welcome to FocusTime!", size="9"),
        rx.text(
            "Your personal Pomodoro companion — stay focused, stay sharp.",
            size="4",
            color="gray"
        ),
        rx.text(
            "\"The key to success is consistency.\"",
            size="3",
            font_style="italic",
            color="gray"
        ),
        rx.input(
            placeholder="Enter your name...",
            width="300px",
            on_change=State.handle_name_change
        ), 
        rx.button(
            "Start Studying",
            on_click=State.start_studying
        ),

        spacing="6",
        justify="center",
        align="center", 
        min_height="100vh",
        background_color="#0D2847",
        padding="4",
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
