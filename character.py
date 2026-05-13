"""
Модуль 1: Класс Character.

Содержит класс персонажа с формулами для человека-героя.
"""
import math 
from unit import Unit


class Character(Unit):
    def __init__(self, strength: int, dexterity: int, constitution: int, wisdom: int, intelligence: int, charisma: int) -> None:
        super().__init__(strength, dexterity, constitution, wisdom, intelligence, charisma)
    
    def calculate_max_health(self) -> int:
        """
        Рассчитать максимальное здоровье персонажа
        """
        return self.constitution * 10 + self.strength//2

    
    def calculate_damage(self) -> int:
        """
        Рассчитать базовый урон персонажа
        """
        return math.floor(self.strength * 1.5 + self.dexterity // 4)

    
    def calculate_defense(self) -> int:
        """
        Рассчитать защиту персонажа
        """
        return math.floor(self.constitution * 1.5 + self.dexterity // 3)