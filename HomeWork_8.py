import sqlite3


def connect_db():
    conn = sqlite3.connect('store.db')
    return conn


def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def create_product(name, price, quantity):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", (name, price, quantity))
    conn.commit()
    conn.close()
    print(f"Товар '{name}' успешно добавлен.")


def read_products():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()
    print("\n--- Список товаров ---")
    for row in rows:
        print(f"ID: {row[0]} | Название: {row[1]} | Цена: {row[2]} | Кол-во: {row[3]}")


# 4. UPDATE — обновление цены по ID
def update_product(id, price):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET price = ? WHERE id = ?", (price, id))
    conn.commit()
    conn.close()
    print(f"Цена товара с ID {id} обновлена на {price}.")


def delete_product(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    print(f"Товар с ID {id} удален.")


if __name__ == "__main__":
    create_table()

    create_product("Laptop", 55000.0, 5)
    create_product("Mouse", 1200.0, 20)

    read_products()

    update_product(1, 52000.0)

    delete_product(2)

    read_products()