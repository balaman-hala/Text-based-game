import health_bar
from health_bar import HealthBar

class Character:
    def __init__(self, name, health, points) -> None:
        self.name = name
        self.health = health
        self.health_max = health
        self.points = points
        
        
        
def attack(self, target) -> None :
    target.health -= self.damage
    target.health = max(target.health, 0)
    
    

class Hero(Character):
    def __init__(self, name, health, points) -> None:
        super().__init__(name = name,
                         health = health,
                         points = points)
        
        self.health_bar = HealthBar(self,color="green")
        
class Enemy(Character):
    def __init__(self, name, health, points) -> None:
        super().__init__(name = name,
                         health = health,
                         points = points)