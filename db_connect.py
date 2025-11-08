import sqlite3

def get_connection():
  conn = sqlite3.connect("app.db")
  return conn
  
# tes koneksi
if __name__ == "__main__":
  conn = get_connection()
  print("Database connected!")
  conn.close()