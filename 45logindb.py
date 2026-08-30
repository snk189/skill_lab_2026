import sqlite3

username = "admin"
password = "1234"

conn = sqlite3.connect("users.db")

result = conn.execute(
    "SELECT * FROM users WHERE username = ?",
    (username,)
)

user = result.fetchone()

conn.close()

if user and user[1] == password:
    print("Login successful!")
else:
    print("Invalid username or password!")