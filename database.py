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
    conn.close()