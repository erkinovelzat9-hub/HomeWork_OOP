class Hero:

    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень: {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1
        print(f"сила героя: {self.strength}")

    def rest(self):
        print(f"{self.name} отдыхает..")
        self.health += 1
        print(f"Здоровье героя: {self.health}\n")


# Первый объект
Kirito = Hero("Кирито", 50, 100, 500)
print(f"Имя: {Kirito.name} \nУровень: {Kirito.level} \nЗдоровья: {Kirito.health}, "
      f"\nсила: {Kirito.strength}")
Kirito.greet()
Kirito.attack()
Kirito.rest()

# Второй объект
Haruna = Hero("Харуна", 10, 50, 100 )
print(f"Имя: {Haruna.name} \nУровень: {Haruna.level} \nЗдоровья: {Haruna.health}, "
      f"\nсила: {Haruna.strength}")
Haruna.greet()
Haruna.attack()
Haruna.rest()


