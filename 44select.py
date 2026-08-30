import sqlite3

conn = sqlite3.connect("users.db")

result = conn.execute(
    "SELECT * FROM users WHERE username = 'admin'"
)

user = result.fetchone()

print(user)

conn.close()