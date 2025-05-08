import reflex as rx

class State(rx.State):
    """The app state."""
    label = "pick a timer or customize one :D"
    label_study = "The study page"
    label_settings = "The settings page"
    label_ranking = "The ranking page"
    label_analytics = "The analytics page"
    label_music = "The music page"


    def handle_input_change(self, val):
        self.label = val
