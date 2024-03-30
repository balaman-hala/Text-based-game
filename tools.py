class Tools:
    def __init__(self, name , damage, type, value ) -> None :
        self.name = name
        self.type = type
        self.damage = damage
        self.value = value
        
        
iron_sword = Tools(name = "Iron Sword",
                   type = "Sharp Weapon",
                   damage = 10,
                   value = 10)


short_bow = Tools(name = "Short Bow",
                  type = "Ranged Weapon",
                  damage = 7,
                  value = 8)

knife = Tools(name = "Knife",
              type = "Sharp",
              damage = 5,
              value = 7)


Lighter = Tools(name = "Lighter",
                damage = 0,
                value = 0,)

Gun = Tools(name = "Gun",
            type = "Hand Gun",
            damage = 15,
            value = 15)