import sqlite3

def create_table():
  conn = sqlite3.connect("app.db")
  cursor = conn.cursor()
  cursor.execute("""
 CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT,
      email TEXT UNIQUE
 ) 
  """)
  conn.commit()
  conn.close()
 
#create user 
def add_user(name, email):
  conn = sqlite3.connect("app.db")
  cursor = conn.cursor()
  cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
  conn.commit()
  conn.close()

#read user
def get_users():
  conn = sqlite3.connect("app.db")
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM users")
  rows = cursor.fetchall()
  conn.close()
  return rows
  
# update user
def update_user(id, name, email):
  conn = sqlite3.connect("app.db")
  cursor = conn.cursor()
  cursor.execute("UPDATE users SET name=?, email=? WHERE id=?", (name, email, id))
  conn.commit()
  conn.close()
  
#delete user
def delete_user(id):
  conn = sqlite3.connect("app.db")
  cursor = conn.cursor()
  cursor.execute("DELETE FROM users WHERE id=?", (id))
  conn.commit()
  conn.close()
  
if __name__ == "__main__":
  create_table()
  add_user("Wahab", "wahab@gmail.com")
  print(get_users())