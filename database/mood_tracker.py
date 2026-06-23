import sqlite3
from datetime import datetime

DB_NAME = "database/mood.db"


def initialize_db():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS moods (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            message TEXT,
            emotion TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_mood(message, emotion):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO moods
        (
            timestamp,
            message,
            emotion
        )
        VALUES (?, ?, ?)
        """,
        (
            datetime.now().isoformat(),
            message,
            emotion
        )
    )

    conn.commit()
    conn.close()