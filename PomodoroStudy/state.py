import reflex as rx

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

