import reflex as rx
from PomodoroStudy.state import State, timer_state
from PomodoroStudy.ui import pomodoro_timer
from PomodoroStudy.ui.base import base_page




def study_page() -> rx.Component:
    # Study Page
    my_child =  rx.vstack(
            rx.heading(State.label_study, size="9"),
            rx.input(
                "Enter Task name",
                size="3",
                on_change=timer_state.handel_task_name,
                
            ),
            rx.input(
                "Enter focus time",
                size="3",
                on_change=timer_state.handel_work_time,

            ),
            rx.input(
                "Enter break time",
                size="3",
                on_change=timer_state.handel_break_time,

            ),
  
            rx.button("Create", on_click=timer_state.add_timer),
            rx.grid(
                rx.center(
                pomodoro_timer.timer_card(),
                height="100vh",
                ),  
                rx.center(
                pomodoro_timer.empty_timer_card(),
                height="100vh",
                ),  
                gap="1rem",
                grid_template_columns=[
                    "1fr",
                    "repeat(2, 1fr)",
                    "repeat(2, 1fr)",
                    "repeat(3, 1fr)",
                    "repeat(4, 1fr)",
                ],
                width="100%",
            ),

            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id="my-child"
        )
              
    return base_page(my_child)