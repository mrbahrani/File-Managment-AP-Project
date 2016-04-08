"""
Thin file including functions for creating needed database and tables .
List of included functions :
1.connect_db
2.create_cash_db
3.add_new_file
4.add_new_directory
5.get_directory_childrens
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
    connection_obj.commit()
    cursor.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER AUTOINCREMENT UNSIGNED PRIMARY KEY,'
                   'user_name VARCHAR,password VARCHAR,server_id VARCHAR(16),port UNSIGNED INT(4),ready_state INT(1)')
    connection_obj.close()


def add_new_user(user_name, password, server_id, port, ready_state):
    """
    | This void function adds a new user to the users table.
    :param user_name:str
    :param password:str
    :param server_id:str
    :param port:id
    :param ready_state:int
    """
    connection_obj = connect_db()
    cursor = connection_obj.cursor()
    query = ((user_name, password, server_id, port, ready_state),)
    cursor.executemany("INSERT INTO users(user_name,password,server_id,port,ready_state)VALUES(?,?,?,?,?)", query)
    connection_obj.commit()
    connection_obj.close()


def validate_user(user_name, password):
    """
    | This function checks if password of a special user_name is correct on not.
    | If yes, returns True, Else reurns False
    :param user_name:str
    :param password:str
    """
    connection_obj = connect_db()
    with connection_obj:
        cursor = connection_obj.cursor()
        execute = cursor.execute("SELECT password FROM users WHERE user_name = '" + user_name + "'")
        saved_password = execute.fetchall()
        if saved_password[0] == password:
            return True
        return False


def change_ready_state(new_state):
    connection_obj = connect_db()
    with connection_obj:
        cursot = connection_obj.cursor()
        