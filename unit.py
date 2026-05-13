"""
Модуль 1: Абстрактный класс Unit и его наследники Character и Monster.

Содержит базовый абстрактный класс для всех игровых юнитов,
а также конкретные реализации для персонажа и монстра.
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