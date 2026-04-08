class Hero:

    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def gree(self):
        print(f"Привет, меня зовут {self.name}")

    def attack(self):
        print(f"Герой {self.name} атакует")
        self.strength -= -10
        print(f"сила: {self.strength}")

    def rest(self):
        print(f"Герой отдыхает")
        self.health += 100
        print(f"Здоровье героя увеличился.\n"
              f"Здоровье: {self.health}")

#











