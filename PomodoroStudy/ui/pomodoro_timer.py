# components/pomodoro.py

import reflex as rx
from reflex.components.radix.themes.base import LiteralAccentColor
from PomodoroStudy.state import State,timer_state

def pomodoro_timer(
    task_name: str,
    time_config_work: int,
    time_config_break: int,
) -> rx.Component:
    badge_color: LiteralAccentColor = "blue"
    is_running = False
    play_pause_icon = "pause" if is_running else "play"
    play_pause_label = "Pause" if is_running else "Start"

    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="timer", size=34),
                    color_scheme=badge_color,
                    radius="full",
                    padding="0.7rem",
                ),
                rx.vstack(
                    rx.heading(time_config_work, size="6", weight="bold"),
                    rx.text(task_name, size="4", weight="medium"),
                    spacing="1",
                    align_items="start",
                    width="100%",
                ),
                spacing="4",
                align="center",
                width="100%",
            ),
            rx.hstack(
                rx.button(
                    rx.icon(tag=play_pause_icon),
                    play_pause_label,
                    on_click=timer_state.toggle_timer(task_name),
                    color_scheme="green" if not is_running else "red",
                    size="3",
                    radius="full",
                ),
                rx.text(
                    f"Work/Break: {time_config_work,time_config_break}",
                    size="2",
                    color=rx.color("gray", 10),
                ),
                align="center",
                spacing="4",
            ),
            spacing="3",
        ),
        size="3",
        width="100%",
        max_width="18rem",
    )



def empty_timer_card() -> rx.Component:
    return rx.card(
        rx.center(
            rx.button(
                rx.icon(tag="plus"),
#                on_click=State.create_new_timer,  # Replace with your actual handler
                size="4",
                radius="full",
                color_scheme="blue",
            ),
            height="7rem",  # Adjust height as needed
        ),
        size="3",
        width="100%",
        max_width="18rem",
        style={"cursor": "pointer"},
    )


def timer_card(name: str, work: int, rest: int):
    return rx.box(
        rx.text(f"Task: {name}"),
        rx.text(f"Work: {work} mins"),
        rx.text(f"Break: {rest} mins"),
        padding="4",
        border="1px solid #ccc",
        border_radius="md",
        box_shadow="md",
    )