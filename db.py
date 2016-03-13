"""
Thin file including functions for creating needed database and tables .
List of included functions :
1.connect_db
"""
from sqlite3 import *


def connect_db():
    """
    | This function make a connection to the FileManager database and returns that;
    :return :sqlite3 connection object
    """
    return connect('data//FileManager.db')


def create_cash_table():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS cash(id INT AUTO INCREMENT UNSIGNED PRIMARY KEY,fod_name VARCHAR(255),'
                   'PARENT TEXT, kind TINYINT(1))')
