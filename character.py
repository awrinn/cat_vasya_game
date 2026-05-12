from unit import Unit


class character(Unit):
    def __init__(self, strength: int, dexterity: int, constitution: int, wisdom: int, intelligence: int, charisma: int):
        self.strength: int = strength
        self.dexterity: int = dexterity
        self.constitutio: int = constitution
        self.wisdom: int = wisdom
        self.intelligence: int = intelligence
        self.charisma: int = charisma
    
    def calculate_max_health(self):
        return self.constitution * 10 + self.strength/2

    
    def calculate_damage(self):
        return self.strength * 1.5 + self.dexterity/4

    
    def calculate_defense(self):
        return self.constitution * 1.5 + dexterity/3    