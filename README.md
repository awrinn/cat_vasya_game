# cat_vasya_game
##  Модули

### Модуль 1 — `unit.py`, `character.py`, `monster.py`
- Абстрактный класс `Unit` с шестью характеристиками
- Класс `Character` (персонаж) с формулами героя
- Класс `Monster` (монстр) с формулами врага
- Все формулы округлены вниз

### Модуль 2 — `module_2_character.py`
- Переработанный класс `Character`
- Поддержка трёх классов: `warrior`, `mage`, `hunter`
- Формулы урона и защиты зависят от выбранного класса

### Модуль 3 — `module_3_spells.py`, обновлённые `unit.py` и `module_2_character.py`
- Абстрактный класс `Spell`
- Три заклинания: `Fireball`, `IceLance`, `LightningBolt`
- У каждого юнита появилась мана (`mana`) и список заклинаний (`spells`)
- Методы `add_spell()` и `cast_spell()`
- У персонажа добавился метод `calculate_max_mana()` (формула зависит от класса)