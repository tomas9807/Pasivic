import os
import sqlite3

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def connect():
    db_path = os.path.join(BASE_DIR,'resources/db/db1.db')
    conn = sqlite3.connect(db_path)
    conn.execute('PRAGMA foreign_keys = ON')
    return conn


