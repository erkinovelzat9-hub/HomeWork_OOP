from abc import ABC, abstractmethod


# 1. Абстрактный класс Hero
class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        # Приватный атрибут (Инкапсуляция)
        self.__health = health
        self.strength = strength

    # Обычный метод
    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    # Метод для работы с приватным атрибутом
    def rest(self):
        print(f"{self.name} отдыхает...")
        self.__health += 1
        print(f"Здоровье увеличено. Текущее здоровье: {self.__health}")

    # Абстрактный метод (Абстракция)
    @abstractmethod
    def attack(self):
        pass


# 2. Дочерние классы
class Warrior(Hero):
    def attack(self):
        print(f"Воин {self.name} атакует мечом!")


class Mage(Hero):
    def attack(self):
        print(f"Маг {self.name} использует магию!")


class Assassin(Hero):
    def attack(self):
        print(f"Ассасин {self.name} атакует из-под тишка!")

# 3. Создание объектов
warrior = Warrior("Ахиллес", 5, 100, 20)
mage = Mage("Мерлин", 7, 60, 15)
assassin = Assassin("Эцио", 6, 80, 25)

# 4. Вызов методов для каждого героя
heroes = [warrior, mage, assassin]

for hero in heroes:
    print("-" * 30)
    hero.greet()
    hero.attack()
    hero.rest()