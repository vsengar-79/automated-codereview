import sqlite3
import config

connection = sqlite3.connect(config.DATABASE)

def get_connection():
    return connection
