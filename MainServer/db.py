"""
Thin file including functions for creating needed database and tables .
List of included functions :
1.connect_db
2.create_cash_db
3.add_new_file
4.add_new_directory
5.get_directory_childrens
"""
import MySqldb as m
from _config import DBHOST, DBNAME, DBPASS, DBUSER


class MySql:
    instance = None
    @staticmethod
    def connection():
        if MySql.instance is None:
            class_instance = MySql()
            MySql.instance = class_instance._connection
        return MySql.instance

    def __init__(self):
        self._connection = m.Connection(DBHOST, DBUSER, DBPASS, DBNAME)


def create_users_table():
    """
    | This void function creates users table if it not exists.
    create_users_table()
    """
    connection_obj = MySql.connection()
    cursor = connection_obj.cursor()
    connection_obj.commit()
    cursor.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,'
                   'user_name VARCHAR(255),password VARCHAR(255),server_id VARCHAR(255),port UNSIGNED INT,'
                   'ready_state INT)')
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
    connection_obj = MySql.connection()
    cursor = connection_obj.cursor()
    query = (user_name, password, server_id, str(port), str(ready_state))
    cursor.executemany("INSERT INTO users(user_name,password,server_id,port,ready_state)VALUES(%s,%s,%s,%s,%s)", query)
    connection_obj.commit()


def validate_user(user_name, password):
    """
    | This function checks if password of a special user_name is correct on not.
    | If yes, returns True, Else reurns False
    :param user_name:str
    :param password:str
    :return boolean
    """
    connection_obj = MySql.connection()
    with connection_obj:
        cursor = connection_obj.cursor()
        cursor.execute("SELECT password FROM users WHERE user_name = %s", (user_name,))
        saved_password = cursor.fetchone()
        try:
            if saved_password[0] == password:
                return True
        finally:
            return False


def change_ready_state(user_name, new_state):
    """
    |This function changes ready state of the user_name;
    |0 is equal to "Not ready for sharing" and 1 is equal to "I'm ready. Let's share!"
    :param user_name:str
    :param new_state:int
    """
    connection_obj = MySql.connection()
    with connection_obj:
        cursor = connection_obj.cursor()
        query = (new_state, user_name)
        cursor.executemany("UPDATE users SET ready_state = %s WHERE user_name = %s", query)
        connection_obj.commit()


def order(provider):
    """
    | This function sends an order request to the provider and if that be ready, gets it's server id and port number.
    | And if that not be ready, returns False.
    :param provider
    :return tuple|boolean
    """
    connection_obj = MySql.connection()
    with connection_obj:
        cursor = connection_obj.cursor()
        cursor.execute("SELECT ready_state FROM user WHERE user_name = %s ", (provider,))
        state = cursor.fetchone()
        if state:
            execute = cursor.execute("SELECT server_id, port FROM users WHERE user_name = %s", (provider,))
            return execute.fetchall()
        return False
