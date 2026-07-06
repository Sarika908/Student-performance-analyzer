import sqlite3

def connect():
    return sqlite3.connect("students.db")

def create_tables():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        class TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS marks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        math INTEGER,
        science INTEGER,
        english INTEGER
    )
    """)

    conn.commit()
    conn.close()

def insert_sample_data():
    conn = connect()
    cursor = conn.cursor()

    cursor.executemany("INSERT INTO students (name, class) VALUES (?, ?)", [
        ("Arun", "10A"),
        ("Divya", "10A"),
        ("Kavin", "10A"),
        ("Meena", "10A"),
        ("Rahul", "10A")
    ])

    cursor.executemany("INSERT INTO marks (student_id, math, science, english) VALUES (?, ?, ?, ?)", [
        (1, 85, 90, 80),
        (2, 70, 75, 72),
        (3, 95, 92, 90),
        (4, 40, 55, 60),
        (5, 60, 65, 58)
    ])

    conn.commit()
    conn.close()