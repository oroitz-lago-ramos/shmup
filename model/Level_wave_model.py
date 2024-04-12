from .Enemy_model import Enemy_model
import time
import random

class Level_wave_model():
    def __init__(self,width,height):
        self.wave = {}
        self.wave_number = 0
        self.screen_width = width
        self.screen_height = height
        self.timer_running = False #True if the timer is running
        self.timer = 0
        self.time_since_last_wave = 0
        self.end = False #True if the level is over
        self.current_ennemy = []
        self.side = None #0 for left, 1 for right
        self.start_timer()
    
    def randomize_side(self):
        self.side = random.randint(0,1)

    def display_position(self):
        if self.side == 0:
            return (-100,random.randint(0,self.screen_height))
        else:
            return ((self.screen_width+100),random.randint(0,self.screen_height))

    def create_wave(self,nb_wave,nb_enemy, player_base_position):
        for i in range(nb_wave):
            self.randomize_side()
            self.wave[i] = []
            for j in range(nb_enemy):
                enemy = Enemy_model(50, 50, 1, 5, (0, 0, 255), 100,player_base_position ,self.display_position()[0], self.display_position()[1])
                #enemy = 1 #test remove for clean code
                self.wave[i].append(enemy)
        return self.wave
    
    def update_wave(self):
        if self.wave_number in self.wave:
            if self.wave[self.wave_number] and self.wave_number != len(self.wave):
                self.add_current_ennemy(self.wave_number)
            else:
                self.wave_number += 1
        
        # print(self.end)


    def update(self,dt, wave_number, ennemy_per_wave, player_base_position):
        """Update the level wave model in the main loop
        param dt: time since last frame
        update the timer and the wave
        """
        if self.wave_number == 0 and self.wave == {}:
            self.create_wave(wave_number, ennemy_per_wave, player_base_position)
        else:
            self.update_timer()
            self.time_since_last_wave += dt
            if self.time_since_last_wave >= 5000:
                self.update_wave()
                self.time_since_last_wave = 0
        for ennemy in self.current_ennemy:
            ennemy.update()
            if ennemy.death:
                self.ennemy_destroyed(ennemy)
        if self.wave_number == len(self.wave) and self.current_ennemy == []:
            self.end = True
        print(self.end)
        print(self.current_ennemy)
        
    def ennemy_destroyed(self, ennemy):
        """Remove the ennemy from the current ennemy list
        use in the main loop to remove the ennemy from the game scene
        """
        self.current_ennemy.remove(ennemy)
        

    def get_wave(self):
        return self.wave

    def get_nb_enemy(self):
        return len(self.wave)
    
    def get_timer(self):
        return self.timer
    
    
    def remove_last_ennemy(self, wave_number):
        """Remove all ennemies of the wave and return it"""
        if wave_number in self.wave and self.wave[wave_number]:
            enemies = self.wave[wave_number]
            self.wave[wave_number] = []
            return enemies

    def add_current_ennemy(self, wave_number):
        """Add the last ennemy of the wave to the current ennemy list
        in order to display it on the game scene
        """
        ennemy = self.remove_last_ennemy(wave_number)
        if ennemy:
            for i in ennemy:

                self.current_ennemy.append(i)
    
    def update_wave_number(self):
        self.wave_number = len(self.wave)

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.time_start = time.time()

    def update_timer(self):
        if self.timer_running:
            time_end = time.time()
            self.timer = round(time_end - self.time_start)
            minutes = self.timer // 60
            seconds = self.timer % 60
            self.timer = f"{minutes:02d} : {seconds:02d}"
        return self.timer
        

