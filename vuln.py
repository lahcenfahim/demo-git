import sqlite3

def search_user(user_input):
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    # Vulnérabilité SQL Injection
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == "__main__":
    user = input("Username: ")
    print(search_user(user))