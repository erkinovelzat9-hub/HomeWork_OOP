import random


# Базовый класс
class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, меня зовут {self.name}!")

    def attack(self):
        print(f"Герой {self.name} атакует!")

    def rest(self):
        self.health += 100
        print(f"Герой отдыхает. Здоровье увеличено до {self.health}")


# Дочерние классы (Наследование)
class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    # Переопределение метода (Полиморфизм)
    def attack(self):
        print(f"Воин {self.name} атакует мечом! (Выносливость: {self.stamina})")


class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(f"Маг {self.name} кастует заклинание! (Мана: {self.mana})")


class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print(f"Ассасин {self.name} атакует из-под тишка! (Скрытность: {self.stealth})")


# Создаем объекты персонажей
warrior_obj = Warrior("Арагорн", 10, 150, 20, 100)
mage_obj = Mage("Гэндальф", 12, 80, 15, 200)
assassin_obj = Assassin("Эцио", 11, 90, 25, 50)

# Словарь для удобного поиска объектов
heroes_dict = {
    "warrior": warrior_obj,
    "mage": mage_obj,
    "assassin": assassin_obj
}

# Переменные для статистики
player_score = 0
bot_score = 0
total_games = 0

print("--- Добро пожаловать в битву героев! ---")
print("Правила: Warrior > Assassin, Assassin > Mage, Mage > Warrior")
print("Для выхода напишите 'выход'")

# Бесконечный цикл игры
while True:
    print(f"\n--- Раунд №{total_games + 1} ---")
    user_choice = input("Выберите героя (Warrior / Mage / Assassin): ").strip().lower()

    # Проверка на выход
    if user_choice == "выход" or user_choice == "exit":
        print("\n--- Игра завершена! ---")
        print(f"Сыграно партий: {total_games}")
        print(f"Итоговый счет -> Вы: {player_score} | Бот: {bot_score}")
        break

    # Проверка правильности ввода
    if user_choice not in heroes_dict:
        print("Такого героя нет! Попробуйте еще раз.")
        continue

    # Выбор игрока и случайный выбор бота
    player = heroes_dict[user_choice]
    enemy_key = random.choice(list(heroes_dict.keys()))
    enemy = heroes_dict[enemy_key]

    print(f"Вы выбрали: {player.__class__.__name__}")
    print(f"Противник выбрал: {enemy.__class__.__name__}")

    total_games += 1

    # Логика определения победителя
    if user_choice == enemy_key:
        print("Результат: Ничья!")
    elif (user_choice == "warrior" and enemy_key == "assassin") or \
            (user_choice == "assassin" and enemy_key == "mage") or \
            (user_choice == "mage" and enemy_key == "warrior"):

        print(f"Результат: Вы победили!")
        player.attack()  # Вызываем метод атаки победителя
        player_score += 1
    else:
        print(f"Результат: Вы проиграли!")
        enemy.attack()  # Вызываем метод атаки бота
        bot_score += 1

    print(f"Текущий счет -> Вы {player_score} : {bot_score} Бот")