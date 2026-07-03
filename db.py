import sqlite3
import os

DB_PATH = "finance.db"

def conn():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init():
    c = conn().cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        category TEXT,
        amount REAL,
        date TEXT
    )
    """)

    conn().commit()
    conn().close()

def add(tx_type, category, amount, date):
    c = conn().cursor()
    c.execute(
        "INSERT INTO transactions (type, category, amount, date) VALUES (?, ?, ?, ?)",
        (tx_type, category, amount, date)
    )
    conn().commit()
    conn().close()

def get_all():
    c = conn().cursor()
    c.execute("SELECT type, category, amount, date FROM transactions")
    rows = c.fetchall()
    conn().close()
    return rows
