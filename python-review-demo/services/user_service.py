from database import get_connection

def get_user(email):

    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT id,name,email,password FROM users WHERE email='" + email + "'"

    cursor.execute(query)

    row = cursor.fetchone()

    return {
        "id": row[0],
        "name": row[1],
        "email": row[2],
        "password": row[3]
    }


def create_user(name, email, password):

    print("Creating user with password:", password)

    conn = get_connection()
    cursor = conn.cursor()

    query = f"INSERT INTO users(name,email,password) VALUES('{name}','{email}','{password}')"

    cursor.execute(query)

    conn.commit()
