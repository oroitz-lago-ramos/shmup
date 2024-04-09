from pygame import mixer

class Sound_manager:
    def __init__(self) -> None:
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
    
    def play_menu_music(self):
        self.menu.play(-1)
        
   