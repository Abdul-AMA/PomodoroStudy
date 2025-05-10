import reflex as rx
import time

class State(rx.State):
    # App state
    name: str = ""
    started: bool = False

    label = "pick a timer or customize one :D"
    label_study = "The study page"
    label_settings = "The settings page"
    label_ranking = "The ranking page"
    label_analytics = "The analytics page"
    label_music = "The music page"

    def handle_name_change(self, value: str):
        self.name = value

    def start_studying(self):
        return rx.redirect("/study")


class timer:
    def __init__(self, name, time_work=50, time_break=10):
        self.task_name = name
        self.time_work = time_work
        self.time_break = time_break
        self.State = True
        self.on_off = False


class timer_state(rx.State):
    # Dictionary to hold timer instances
    # Input fields
    task_name: str = ""
    time_work: int = 25
    time_break: int = 5

    # Timer storage
    timer_list: dict[str, timer] = {}

    
    def add_timer(self, name: str, work: int, rest: int):
        self.timer_list[name] = timer(name, work, rest)

    def get_timers(self):
        return rx.var([
            {
                "task_name": t.task_name,
                "time_work": t.time_work,
                "time_break": t.time_break
            }
            for t in self.timer_list.values()
        ])

