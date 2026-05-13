"""
Модуль 3: Заклинания и магия.

Содержит:
- абстрактный класс Spell
- три конкретных заклинания: Fireball, IceLance, LightningBolt
"""
from abc import ABC, abstractmethod

class Spell(ABC):
    def __init__(self, name: str, damage: int, mana_cost: int) -> None:
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

    @abstractmethod
    def cast(self) -> int:
        """
        Применить заклинание, вернуть урон
        """
        pass


class Fireball(Spell):
    """
    Огненный шар: урон 35, мана 15
    """

    def __init__(self) -> None:
        super().__init__("Огненный шар", 35, 15)

    def cast(self) -> int:
        return self.damage


class IceLance(Spell):
    """
    Ледяное копьё: урон 25, мана 10
    """

    def __init__(self) -> None:
        super().__init__("Ледяное копьё", 25, 10)

    def cast(self) -> int:
        return self.damage


class LightningBolt(Spell):
    """
    Разряд молнии: урон 40, мана 20
    """

    def __init__(self) -> None:
        super().__init__("Разряд молнии", 40, 20)

    def cast(self) -> int:
        return self.damage