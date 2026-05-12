from unit import Unit


class monster(Unit):
    def __init__(self, strength: int, dexterity: int, constitution: int, wisdom: int, intelligence: int, charisma: int):
        self.strength: int = strength
        self.dexterity: int = dexterity
        self.constitutio: int = constitution
        self.wisdom: int = wisdom
        self.intelligence: int = intelligence
        self.charisma: int = charisma
    
    def calculate_max_health(self):
       return self.constitution * 8 + self.strength/3

    
    def calculate_damage(self):
        return self.strength * 2 + self.dexterity/5

    
    def calculate_defense(self):
        return self.constitution * 1.2 + dexterity/5  