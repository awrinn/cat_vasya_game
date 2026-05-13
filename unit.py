"""
Модуль 3: В Unit добавилось 2 атрибута и 2 метода
"""
from abc import ABC, abstractmethod

class Unit(ABC):
    """
    Абстрактный базовый класс для всех игровых юнитов.

    Атрибуты:
        strength (int): Сила 
        dexterity (int): Ловкость 
        constitution (int): Телосложение 
        wisdom (int): Мудрость 
        intelligence (int): Интеллект 
        charisma (int): Харизма 
    """
    def __init__(self, strength: int, dexterity: int, constitution: int, wisdom: int, intelligence: int, charisma: int) -> None:
         """
        Инициализация юнита с шестью базовыми характеристиками.

        Args:
            strength: Сила юнита
            dexterity: Ловкость юнита
            constitution: Телосложение юнита
            wisdom: Мудрость юнита
            intelligence: Интеллект юнита
            charisma: Харизма юнита
        """
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma
        self.spells = []
        self.mana = 0

    @abstractmethod
    def calculate_max_health(self) -> int:
        """
        Рассчитать и вернуть максимальное здоровье юнита
        """
        pass

    @abstractmethod
    def calculate_damage(self) -> int:
        """
        Рассчитать и вернуть базовый урон юнита
        """
        pass

    @abstractmethod
    def calculate_defense(self) -> int:
        """
        Рассчитать и вернуть показатель защиты юнита.
        """
        pass
    
    def add_spell(self, spell):
        """
        Добавить заклинание
        """
        self.spells.append(spell)

    def cast_spell(self, index):
        """Применить заклинание по индексу
        """
        if index >= len(self.spells):
            raise IndexError("Нет такого заклинания")

        spell = self.spells[index]

        if self.mana >= spell.mana_cost:
            self.mana -= spell.mana_cost
            return spell.cast()
        else:
            raise ValueError("Не хватает маны")