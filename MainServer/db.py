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


def create_users_table():
    """
    | This void function creates users table if it not exists.
    create_users_table()
    """
    connection_obj = connect_db()
    cursor = connection_obj.cursor()
    connection_obj.commit()
    cursor.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER AUTOINCREMENT UNSIGNED PRIMARY KEY,'
                   'user_name TEXT,password TEXT,server_id TEXT,port UNSIGNED INT(4),ready_state INT(1)')
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
    :return boolean
    """
    connection_obj = connect_db()
    with connection_obj:
        cursor = connection_obj.cursor()
        execute = cursor.execute("SELECT password FROM users WHERE user_name = '" + user_name + "'")
        saved_password = execute.fetchall()
        if saved_password[0] == password:
            return True
        return False


def change_ready_state(user_name, new_state):
    """
    |This function changes ready state of the user_name;
    |0 is equal to "Not ready for sharing" and 1 is equal to "I'm ready. Let's share!"
    :param user_name:str
    :param new_state:int
    """
    connection_obj = connect_db()
    with connection_obj:
        cursor = connection_obj.cursor()
        query = ((new_state, user_name), )
        execute = cursor.executemany("UPDATE users SET ready_state = ? WHERE user_name = ?", query)
        connection_obj.commit()


def order(provider):
    """
    | This function sends an order request to the provider and if that be ready, gets it's server id and port number.
    | And if that not be ready, returns False.
    :param provider
    :return tuple|boolean
    """
    connection_obj = connect_db()
    with connection_obj:
        cursor = connection_obj.cursor()
        execute = cursor.execute("SELECT ready_state FROM user WHERE user_name = " + provider)
        state = execute.fetchall()
        if state:
            execute = cursor.execute("SELECT server_id, port FROM users WHERE user_name = " + provider)
            return execute.fetchall()
        return False
