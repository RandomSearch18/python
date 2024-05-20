"""A based data-based database manager"""

from pathlib import Path
import sqlite3

from colorama import Style

from menu import Menu, Page, bold, color
from inputs import decimal, integer, integer_range, text


class Database:
    def __init__(self, file: Path) -> None:
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()

    def __del__(self) -> None:
        self.connection.close()

    def create_table_if_not_exists(self, table_name: str, sql: str) -> None:
        self.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
            (table_name,),
        )
        if self.cursor.fetchone() is not None:
            return
        self.cursor.execute(sql)
        print(f"Created table {table_name}")

    # def insert(self, table_name: str, **kwargs) -> None:
    #     sql = "INSERT INTO ? (?) VALUES "

    def insert_product(self, name: str, price: float) -> None:
        self.cursor.execute(
            "INSERT INTO Product (name, price) VALUES (?, ?)", (name, price)
        )
        self.connection.commit()


print("Loading database file...")
database = Database(Path("coffee_shop.db"))

print("Ensuring database is ready...")
database.create_table_if_not_exists(
    "Product",
    """
    CREATE TABLE Product (
        id INTEGER,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        PRIMARY KEY (id)
    )
    """,
)


def add_product():
    name = text("Product name: ").capitalize()
    price = decimal("Price: £")
    database.insert_product(name, price)
    print()
    print(f"Added product {bold(name)} with price {bold(f'£{price:.2f}')}")


def format_product_data(product_data):
    id, name, price = product_data
    return f"{color(f'{id:04}', Style.DIM)} {name} - £{price:.2f}"


def list_products():
    products = database.cursor.execute("SELECT * FROM Product").fetchall()
    for product_data in products:
        print(format_product_data(product_data))


def delete_product():
    selected_id = integer("Product ID to delete: ")

    print()


def show_main_menu():
    main_menu = Menu(
        [
            Page(
                "Add product",
                add_product,
            ),
            Page(
                "List products",
                list_products,
            ),
        ],
        title="Coffee shop management system",
    )

    main_menu.show(loop=True)


if __name__ == "__main__":
    show_main_menu()
