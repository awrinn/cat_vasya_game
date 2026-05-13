"""
Модуль 1: Класс Monster.

Содержит класс персонажа с формулами для монстра.
"""
import math
from unit import Unit


class Monster(Unit):
    def __init__(self, strength: int, dexterity: int, constitution: int, wisdom: int, intelligence: int, charisma: int) -> None:
        super().__init__(strength, dexterity, constitution, wisdom, intelligence, charisma)
    
    def calculate_max_health(self):
        """
        Рассчитать максимальное здоровье монстра.
        """
       return self.constitution * 8 + self.strength//3

    
    def calculate_damage(self):
        """
        Рассчитать базовый урон монстра.
        """
        return math.floor(self.strength * 2 + self.constitution // 5)

    
    def calculate_defense(self):
        """
        Рассчитать защиту монстра.
        """
        return smath.floor(self.constitution * 1.2 + self.strength // 5)  