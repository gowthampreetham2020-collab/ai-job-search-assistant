<<<<<<< HEAD
import sqlite3

def init_db():

    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS applications(
        id INTEGER PRIMARY KEY,
        company TEXT,
        role TEXT
    )
    """)

    conn.commit()
=======
import sqlite3

def init_db():

    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS applications(
        id INTEGER PRIMARY KEY,
        company TEXT,
        role TEXT
    )
    """)

    conn.commit()
>>>>>>> e964efba0d8a6b86fee83d400bb44c95b9fe409f
    conn.close()