from model.Enemy_model import Enemy_model

class Level_wave_model():
    def __init__(self,width,height):
        self.wave = []
        self.screen_width = width
        self.screen_height = height
        self.level = 1


    def create_wave(self,nb_wave,nb_enemy):
        for i in range(nb_wave):
            for j in range(nb_enemy):
                enemy = Enemy_model(50, 50, 1, 5, (255, 0, 0), 100,(self.screen_width,self.screen_height))
                self.wave.append(enemy)
        print(self.wave)
        return self.wave

