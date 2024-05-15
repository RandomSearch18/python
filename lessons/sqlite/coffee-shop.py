"""A based data-based database manager"""

from pathlib import Path
import sqlite3


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


database = Database(Path("coffee_shop.db"))

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

# database.insert_product("Espresso", 1.5)
# print("Added Espresso")
