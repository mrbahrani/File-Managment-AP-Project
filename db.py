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
    """
    | This void function creates cash table if it not exists.
    create_cash_table()
    """
    connection_obj = connect_db()
    cursor = connection_obj.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS cash(id INTEGER AUTOINCREMENT UNSIGNED PRIMARY KEY,fod_name INT(5),'
                   'parent TEXT,kind TINYINT(1),fod_size INT UNSIGNED,Ctime DATETIME,mode CHAR(10),cash_date DATETIME)')
    connection_obj.commit()
    connection_obj.close()


def add_new_file(file_name, parent_path, size, create_time, file_mode, cash_date):
    """
    | This void function adds a new file to the cash table.
    :param file_name:str
    :param parent_path:str
    :param size:int
    :param create_time:str
    :param file_mode :int
    :param cash_date:str
    """
    connection_obj = connect_db()
    cursor = connection_obj.cursor()
    query = ((file_name, parent_path, 1, size, create_time, file_mode, cash_date),)
    cursor.executemany("INSERT INTO cash(fod_name,parent,kind,fod_size,Ctime,mode,cash_date) VALUES(?,?,?,?,?,?,?)", query)
    connection_obj.commit()
    connection_obj.close()

