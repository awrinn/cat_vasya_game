"""
Модуль 2: Класс Character с выбором класса (воин, маг, охотник).
"""

import math
from unit import Unit


class Character(Unit):
    """
    Класс персонажа с поддержкой игровых классов:
    - warrior (воин)
    - mage (маг)
    - hunter (охотник)
    """

    def __init__(self, strength: int, dexterity: int, constitution: int, wisdom: int, intelligence: int, charisma: int, character_class: str) -> None:
        super().__init__(strength, dexterity, constitution, wisdom, intelligence, charisma)

        if character_class not in ['warrior', 'mage', 'hunter']:
            raise ValueError("Класс должен быть: warrior, mage или hunter")

        self.character_class = character_class

        self.max_health = self.calculate_max_health()
        self.current_health = self.max_health
        self.damage = self.calculate_damage()
        self.defense = self.calculate_defense()

    def calculate_max_health(self) -> int:
        """
        Здоровье для всех классов одинаковое
        """
        return self.constitution * 10 + self.strength // 2

    def calculate_damage(self) -> int:
        """
        Урон зависит от класса
        """
        if self.character_class == 'warrior':
            return math.floor(self.strength * 2.2 + self.constitution // 3)
        elif self.character_class == 'mage':
            return math.floor(self.intelligence * 2.5 + self.wisdom // 2)
        else:  # hunter
            return math.floor(self.dexterity * 1.9 + self.strength // 3)

    def calculate_defense(self) -> int:
        """
        Защита зависит от класса
        """
        if self.character_class == 'warrior':
            return math.floor(self.constitution * 1.8 + self.strength // 4)
        elif self.character_class == 'mage':
            return math.floor(self.wisdom * 1.3 + self.intelligence // 6)
        else:  # hunter
            return math.floor(self.dexterity * 1.6 + self.constitution // 5)