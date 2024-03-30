class Character:
    def __init__(self, name, health, points, damage) -> None:
        self.name = name
        self.health = health
        self.damage = damage
        self.points = points
        
        
        
def attack(self, target) -> None :
    target.health -= self.damage
    target.health = max(target.health, 0)
    
    

class Hero(Character):
    def __init__(self, name, health, points) -> None:
        super().__init__(name = name,
                         health = health,
                         points = points)
        
        
class Enemy(Character):
    def __init__(self, name, health, points) -> None:
        super().__init__(name = name,
                         health = health,
                         points = points)