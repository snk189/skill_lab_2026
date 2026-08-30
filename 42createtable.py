import sqlite3

conn = sqlite3.connect("users.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    password TEXT
)
""")

conn.close()