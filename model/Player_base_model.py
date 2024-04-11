from model import Entity_model
class Player_base_model(Entity_model):
    def __init__(self, color, x, y, width, height, max_health):
        super().__init__(color, x, y, width, height)
        self.max_health = max_health
        self.health = max_health
        self.planet_radius = 172
        self.death = False
        
    def get_health(self):
        return self.health
    def take_damage(self, damage):
        self.health -= damage
    def check_if_alive(self):
        if self.health <= 0:
            self.death = True
    
    def update(self):
        self.check_if_alive()
    