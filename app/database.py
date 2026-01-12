# app/database.py

import mysql.connector

def get_connection():
    """
    Returns a MySQL connection object.
    Make sure to replace password with your MySQL password.
    """
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Prachi@61",  # <-- Replace this
        database="scraping_db"
    )

