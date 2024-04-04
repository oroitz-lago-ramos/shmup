from views import View_interface
class End_menu_view(View_interface):
    def __init__(self, game) -> None:
        self.game = game
    
    def draw(self) -> None:
        pass
    
    def handle_event(self, event) -> None:
        pass
    