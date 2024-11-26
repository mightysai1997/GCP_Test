import sqlite3

def get_user_details(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Unsafely construct the query with string concatenation
    query = f"SELECT * FROM users WHERE username = '{username}';"
    cursor.execute(query)
    
    result = cursor.fetchone()
    conn.close()
    return result

# Attacker can input: ' OR '1'='1
username = input("Enter username: ")
details = get_user_details(username)
print(details)
