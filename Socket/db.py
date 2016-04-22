from sqlite3 import *


def connect_db():
    """
    | This function make a connection to the userDatabase database and returns that;
    :return :sqlite3 connection object
    """
    return connect('data//userDatabase.db')


def create_settings_table():
    """
    | This void function creates users table if it not exists.
    create_users_table()
    """
    connection_obj = connect_db()
    cursor = connection_obj.cursor()
    connection_obj.commit()
    cursor.execute('CREATE TABLE IF NOT EXISTS settings(id INTEGER AUTOINCREMENT UNSIGNED PRIMARY KEY,'
                   'setting_name VARCHAR(255),setting_value VARCHAR(255)')
    connection_obj.close()


def get_setting_value(setting_name):
    """
    | This function returns the value of specific setting .
    :param setting_name str
    :return str
    """
    connection_obj = connect_db()
    cursor = connection_obj.cursor()
    execute = cursor.execute("SELECT password FROM users WHERE setting_name = '" + setting_name + "'")
    setting_value = execute.fetchall()
    connection_obj.close()
    return setting_value[0]


def set_setting(setting_name, setting_value):
    """
    | This function sets a setting name and value.If that setting_name exists, updates it's value, Otherwise
    | Insert that to the table
    :param setting_name str
    :param setting_value str
    """
    connection_obj = connect_db()
    cursor = connection_obj.cursor()
    if get_setting_value(setting_name):
        cursor.execute("UPDATE settings SET setting_value = '" +setting_value + "' WHERE setting_name = '" + setting_name +"'")
        cursor.commit()
    else:
        cursor.execute('INSERT INTO settings(setting_name,setting_value) VALUES ( '+ 'setting_name' + ','+'setting_value' +')')
        cursor.commit()
    connection_obj.close()