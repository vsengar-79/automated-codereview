import sqlite3
import config

connection = sqlite3.connect(config.DBASE)

def get_connection():
    return conection
