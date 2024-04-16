from pygame import mixer
from view_model import View_state

class Sound_manager:
    """A class that manages the sound of the game"""
    def __init__(self, game) -> None:
        self.game = game
        mixer.init()
        mixer.set_num_channels(32)
        
        self.menu = mixer.Sound("./assets/vfx/musics/main_theme.wav")
        self.menu.set_volume(0.1)
        self.menu.play(-1)
        
        self.hall_of_fame = mixer.Sound("./assets/vfx/musics/hall_of_fame.wav")
        self.hall_of_fame.set_volume(0.1)
        
        self.start_sound = mixer.Sound("./assets/vfx/sounds/start_sound.wav")
        self.start_sound.set_volume(0.2)
        
        self.click = mixer.Sound("./assets/vfx/sounds/click.wav")
        self.click.set_volume(0.2)

        self.shoot = mixer.Sound("./assets/vfx/sounds/laser-gun-shot.mp3")
        self.shoot.set_volume(0.1)
        
    def play_menu_music(self):
        """Play the menu music"""
        self.menu.play(-1)
    
    def play_music(self):
        """Play the music of the game according to the current view state"""
        if isinstance(self.game.current_view, self.game.VIEW_STATES[View_state.START_MENU]):
            pass
        elif isinstance(self.game.current_view, self.game.VIEW_STATES[View_state.MAIN_MENU]):
            self.hall_of_fame.stop()
        elif isinstance(self.game.current_view, self.game.VIEW_STATES[View_state.GAME]):
            self.menu.stop()
            self.hall_of_fame.stop()
        elif isinstance(self.game.current_view, self.game.VIEW_STATES[View_state.HALL_OF_FAME]):
            self.menu.stop()
            self.hall_of_fame.play(-1)
    
    def play_start_sound(self):
        """Play the start sound of the game"""
        self.start_sound.play()
    def play_click_sound(self):
        """Play the click sound of the game"""
        self.click.play()
    def play_shoot_sound(self):
        """Play the shoot sound of the game"""
        self.shoot.play()
        
        
   