from model.Entity_model import Entity_model

class Canon_model(Entity_model):
    """A class that represents a canon in the game. It inherits from the Entity_model class.
    arg: x, y, width, height, color, direction
    attributes: x, y, width, height, color, direction, projectiles_list"""
    def __init__(self, x, y, width, height, color, direction):
        super().__init__(color, x, y, width, height)
        self.direction = direction
        self.projectiles_list= []
    
    def set_projectiles_list(self, projectiles_list):
        """Set the projectiles list of the canon
        arg: projectiles_list
        appends the projectiles_list to the canon's projectiles_list"""
        self.projectiles_list.append(projectiles_list)
    
    def get_projectiles_list(self):
        return self.projectiles_list

    def set_direction(self, direction):
        self.direction = direction.normalize()

    def get_direction(self):
        return self.direction
    
    def get_position(self):
        return self.x, self.y
    
    def set_position(self, x, y):
        self.x = x
        self.y = y

    def shoot(self):
        pass

    def update(self, x, y):
        self.x = x
        self.y = y
        

    def update_projectiles(self):
        pass
        
