import sqlite3
import os
from contextlib import closing
from dotenv import load_dotenv


load_dotenv()


def connect(db_path=os.getenv('DB_PATH')):
    return sqlite3.connect(db_path)


def create_db_if_not_exist():
    with connect() as conn, closing(conn.cursor()) as cur:
        cur.execute('''CREATE TABLE IF NOT EXISTS rooms (id INTEGER, price_byn REAL, price_usd REAL, parameters TEXT, address TEXT, short_description TEXT, url TEXT, hash_id TEXT PRIMARY KEY)''')


def add_new_item(post_id, price_byn, price_usd, parameters, address, short_description, url, hash_id):
    create_db_if_not_exist()
    with connect() as conn, closing(conn.cursor()) as cur:
        cur.execute('''INSERT OR IGNORE INTO rooms (id, price_byn, price_usd, parameters, address, short_description, url, hash_id)
        VALUES (?, ?, ?, ? ,? ,? ,?, ?)''', (post_id, price_byn, price_usd, parameters, address, short_description, url, hash_id))
        affected = cur.rowcount
        if affected > 0:
            return True
