from pygame import mixer
from view_model import View_state

class Sound_manager:
    def __init__(self, game) -> None:
        self.game = game
        mixer.init()
        # self.background = mixer.Sound("assets/sound/background.wav")
        # self.background.set_volume(0.1)
        # self.background.play(-1)
        # self.shoot = mixer.Sound("assets/sound/shoot.wav")
        # self.shoot.set_volume(0.1)
        # self.explosion = mixer.Sound("assets/sound/explosion.wav")
        # self.explosion.set_volume(0.1)
        # self.hit = mixer.Sound("assets/sound/hit.wav")
        # self.hit.set_volume(0.1)
        # self.game_over = mixer.Sound("assets/sound/game_over.wav")
        # self.game_over.set_volume(0.1)
        # self.win = mixer.Sound("assets/sound/win.wav")
        # self.win.set_volume(0.1)
        self.menu = mixer.Sound("./assets/vfx/musics/main_theme.wav")
        self.menu.set_volume(0.1)
        self.menu.play(-1)
        
        self.start_sound = mixer.Sound("./assets/vfx/sounds/start_sound.wav")
        self.start_sound.set_volume(0.2)
        
        self.click = mixer.Sound("./assets/vfx/sounds/click.wav")
        self.click.set_volume(0.2)
        
    
    def play_menu_music(self):
        self.menu.play(-1)
    
    def play_music(self):
        if isinstance(self.game.current_view, self.game.VIEW_STATES[View_state.START_MENU]):
            pass
        elif isinstance(self.game.current_view, self.game.VIEW_STATES[View_state.MAIN_MENU]):
            pass
        elif isinstance(self.game.current_view, self.game.VIEW_STATES[View_state.GAME]):
            self.menu.stop()
        elif isinstance(self.game.current_view, self.game.VIEW_STATES[View_state.END_MENU]):
            pass
    
    def play_start_sound(self):
        self.start_sound.play()
    def play_click_sound(self):
        self.click.play()
        
        
   