from pathlib import Path
import sqlite3


class Database:
    def __init__(self, file: Path) -> None:
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()

    def create_table_if_not_exists(self, table_name: str, sql: str) -> None:
        self.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
            (table_name,),
        )
        if self.cursor.fetchone() is not None:
            return
        self.cursor.execute(sql)
        print(f"Created table {table_name}")


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
