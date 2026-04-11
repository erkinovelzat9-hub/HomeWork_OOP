rates = {
    "KGS": 1,
    "USD": 89,
    "EUR": 96,
    "RUB": 1.2
}


class Money:
    def __init__(self, amount, currency):
        if currency not in rates:
            raise ValueError("Неизвестная валюта")
        self.amount = amount
        self.currency = currency

    def convert_to_kgs(self):
        return self.amount * rates[self.currency]

    def convert_to(self, new_currency):
        if new_currency not in rates:
            raise ValueError("Неизвестная валюта")
        kgs = self.convert_to_kgs()
        return Money(kgs / rates[new_currency], new_currency)

    def from_kgs(self, amount_kgs):
        return Money(amount_kgs / rates[self.currency], self.currency)

    def __add__(self, other):
        if isinstance(other, Money):
            total = self.convert_to_kgs() + other.convert_to_kgs()
            return self.from_kgs(total)
        raise TypeError("Можно складывать только с Money")

    def __sub__(self, other):
        if isinstance(other, Money):
            total = self.convert_to_kgs() - other.convert_to_kgs()
            return self.from_kgs(total)
        raise TypeError("Можно вычитать только с Money")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.amount * other, self.currency)
        raise TypeError("Можно умножать только на число")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Деление на ноль!")
            return Money(self.amount / other, self.currency)
        raise TypeError("Можно делить только на число")

    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"



def input_number(text):
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("Ошибка! Введите число.")


def input_currency():
    while True:
        cur = input("Введите валюту (KGS/USD/EUR/RUB): ").upper()
        if cur in rates:
            return cur
        else:
            print("Ошибка! Неверная валюта.")


def create_money():
    amount = input_number("Введите сумму: ")
    currency = input_currency()
    return Money(amount, currency)



while True:
    print("\n--- МЕНЮ ---")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Конвертация")
    print("0. Выход")

    choice = input("Выберите действие: ")

    try:
        if choice == "0":
            print("Выход 👋")
            break

        elif choice in ["1", "2"]:
            print("Введите первую сумму:")
            m1 = create_money()
            print("Введите вторую сумму:")
            m2 = create_money()

            if choice == "1":
                print("Результат:", m1 + m2)
            else:
                print("Результат:", m1 - m2)

        elif choice == "3":
            m = create_money()
            num = input_number("Введите число: ")
            print("Результат:", m * num)

        elif choice == "4":
            m = create_money()
            num = input_number("Введите число: ")
            print("Результат:", m / num)

        elif choice == "5":
            m = create_money()
            new_currency = input_currency()
            print("Результат:", m.convert_to(new_currency))

        else:
            print("Неверный выбор!")

    except Exception as e:
        print("Ошибка:", e)