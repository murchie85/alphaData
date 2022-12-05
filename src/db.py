import sqlite3

def create_database():
    # create a new database if one does not already exist
    conn = sqlite3.connect("mydatabase.db")

    # create a table
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")

    # save the changes
    conn.commit()
    conn.close()

def insert_user(name, email):
    # connect to the database
    conn = sqlite3.connect("mydatabase.db")

    # insert a new user
    conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))

    # save the changes
    conn.commit()
    conn.close()

def read_data():
    # connect to the database
    conn = sqlite3.connect("mydatabase.db")

    # read the data
    cursor = conn.execute("SELECT * FROM users")
    for row in cursor:
        print(row)

    conn.close()

def update_user(name, id):
    # connect to the database
    conn = sqlite3.connect("mydatabase.db")

    # update the user's name
    conn.execute("UPDATE users SET name = ? WHERE id = ?", (name, id))

    # save the changes
    conn.commit()
    conn.close()

def delete_user(id):
    # connect to the database
    conn = sqlite3.connect("mydatabase.db")

    # delete the user
    conn.execute("DELETE FROM users WHERE id = ?", (id,))

    # save the changes
    conn.commit()
    conn.close()

# create the database and table
create_database()

# insert a new user
insert_user("Jane Doe", "jane.doe@example.com")

# read the data
read_data()

# update the user's name
update_user("Jane Smith", 1)

# delete the user
delete_user(1)
