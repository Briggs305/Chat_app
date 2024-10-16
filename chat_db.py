import sqlite3

def show_all():
    # CREATE CONNECTION
    conn = sqlite3.connect('chat.db')

    # Create a cursor/instance
    c = conn.cursor()

    # query the database
    c.execute("SELECT rowid, * FROM chats")
    items = c.fetchall()

    for item in items:
        print(item)
        # commit changes
    conn.commit()
    # close connection
    conn.close()


def sign_up(name, password, passkey):
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute('''INSERT INTO chats (name, password, passkey) VALUES (?, ?, ?)
        ''', (name, password, passkey))

    conn.commit()
    print("User signed up successfully...")
    conn.close()


def login(passkey):
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM chats WHERE passkey = ?
    ''', (passkey,))
    chat = c.fetchone()

    if chat:
        print("Login successful. Welcome, {}!".format(chat[1]))  # user[1] is the name
    else:
        print("Login failed: Invalid passkey.")
        conn.commit()
        conn.close()


def delete(passkey):
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute('''DELETE FROM chats WHERE passkey = (?) ''', passkey)
    chat = c.fetchone()
    # commit changes
    conn.commit()
    # close conections
    conn.close()




def name_lookup(name):
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers WHERE name = (?) ", (name,) )
    items = c.fetchall()

    for item in items:
        print(item)

    # commit changes
    conn.commit()
    # close conections
    conn.close()