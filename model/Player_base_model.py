from model import Entity_model
class Player_base_model(Entity_model):
    def __init__(self, color, x, y, width, height, max_health):
        super().__init__(color, x, y, width, height)
        self.max_health = max_health
        self.health = max_health
        self.planet_radius = 172
        self.death = False
        
        self.cooldown = 15000
        self.bomb_available = True
        self.time_since_last_bomb = 0
        self.current_cooldown = 0
        
    def get_health(self):
        return self.health
    def take_damage(self, damage):
        self.health -= damage
    def check_if_alive(self):
        if self.health <= 0:
            self.death = True
    
    def update(self,dt):
        self.check_if_alive()
        self.update_bomb(dt)
        
    def update_bomb(self, dt):
        if not self.bomb_available:
            self.time_since_last_bomb += dt
            self.current_cooldown = self.cooldown - self.time_since_last_bomb
            if self.time_since_last_bomb >= self.cooldown:
                self.bomb_available = True
                self.time_since_last_bomb = 0
                self.current_cooldown = 0

    def use_bomb(self, enemies):
        if self.bomb_available:
            for enemy in enemies:
                if enemy.second_phase:
                    enemy.kill()
            self.bomb_available = False
            self.time_since_last_bomb = 0
        
    