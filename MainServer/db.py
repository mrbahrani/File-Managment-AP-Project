"""
Thin file including functions for creating needed database and tables .
List of included functions :
1.connect_db
2.create_cash_db
3.add_new_file
4.add_new_directory
5.get_directory_childrens
"""
import MySQLdb as m
from _config import DBHOST, DBNAME, DBPASS, DBUSER


def get_connection():
    """
    | This function returns a connection object with _config file information.
    :return: connection object
    """
    connection = m.Connect(DBHOST, DBUSER, DBPASS, DBNAME)
    connection.set_character_set('utf8')
    cursor = connection.cursor()
    cursor.execute('SET NAMES utf8;')
    cursor.execute('SET CHARACTER SET utf8;')
    cursor.execute('SET character_set_connection=utf8;')
    return connection


def create_users_table():
    """
    | This void function creates users table if it not exists.
    create_users_table()
    """
    connection_obj = get_connection()
    cursor = connection_obj.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTO_INCREMENT,'
                   'user_name VARCHAR(255),password VARCHAR(255),server_id VARCHAR(255),port INT,'
                   'ready_state INT)')
    connection_obj.commit()
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
    connection_obj = get_connection()
    cursor = connection_obj.cursor()
    if cursor.execute("SELECT id FROM users WHERE user_name = %s", (user_name,)):
        return "1|"
    query = (user_name, password, server_id, str(port), str(ready_state))
    print "kir"
    print "INSERT INTO users(user_name,password,server_id,port,ready_state)VALUES(%s,%s,%s,%s,%s)"%query
    cursor.execute("INSERT INTO users(user_name,password,server_id,port,ready_state)VALUES(%s,%s,%s,%s,%s)", query)
    connection_obj.commit()


def validate_user(user_name, password):
    """
    | This function checks if password of a special user_name is correct on not.
    | If yes, returns True, Else reurns False
    :param user_name:str
    :param password:str
    :return boolean
    """
    connection_obj = get_connection()
    with connection_obj:
        cursor = connection_obj.cursor()
        cursor.execute("SELECT password FROM users WHERE user_name = %s", (user_name,))
        saved_password = cursor.fetchone()
        print saved_password
        print password
        print 'kk'
        try:
            if saved_password[0] == str(password):
                return True
        except IndexError:
            return False


def change_ready_state(user_name, new_state):
    """
    |This function changes ready state of the user_name;
    |0 is equal to "Not ready for sharing" and 1 is equal to "I'm ready. Let's share!"
    :param user_name:str
    :param new_state:int
    """
    connection_obj = get_connection()
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
    connection_obj = get_connection()
    with connection_obj:
        cursor = connection_obj.cursor()
        cursor.execute("SELECT ready_state FROM users WHERE user_name = %s ", (provider,))
        state = cursor.fetchone()
        if state:
            cursor.execute("SELECT server_id, port FROM users WHERE user_name = %s", (provider,))
            return cursor.fetchone()
        return False


def change_user_connection_info(user_name, server_ip, port):
    connection_obj = get_connection()
    with connection_obj:
        cursor = connection_obj.cursor()
        cursor.execute("UPDATE users SET server_id = %s,port=%s WHERE user_name = %s", (server_ip, port, user_name))
        connection_obj.commit()
        return True
