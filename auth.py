import sqlite3
import hashlib

def hash_password(password):
  return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
  conn = sqlite3.connect("app.db")
  cursor = conn.cursor()
  cursor.execute("""
      CREATE TABLE IF NOT EXISTS accounts (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          username TEXT UNIQUE,
          password TEXT
      )
  """)
  conn.commit()
  try:
    cursor.execute("INSERT INTO accounts (username, password) VALUES (?, ?)", (username, hash_password(password)))
    conn.commit()
    print("Registrasi berhasil!")
  except sqlite3.IntegrityError:
    print("Username sudah terdaftar")
    
def login(username, password):
  conn = sqlite3.connect("app.db")
  cursor = conn.cursor()
  cursor.execute("SELECT password FROM accounts WHERE username=?", (username,))
  row = cursor.fetchone()
  conn.close()
  if row and row[0] == hash_password(password):
    print("Login berhasil")
    return True
  else:
    print("Username atau password salah")
    return False
    
if __name__ == "__main__":
  register("wahab", "12345")
  login("wahab", "12345")