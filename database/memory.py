import sqlite3

DB_NAME = "database/mood.db"


def initialize_memory():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            memory TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_memory(text):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO memories
        (memory)
        VALUES (?)
        """,
        (text,)
    )

    conn.commit()
    conn.close()


def get_memories():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT memory
        FROM memories
        ORDER BY id DESC
        LIMIT 5
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return [
        row[0]
        for row in rows
    ]