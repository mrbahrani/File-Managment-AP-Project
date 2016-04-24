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
    cursor.execute('CREATE TABLE IF NOT EXISTS settings(id INTEGER PRIMARY KEY AUTOINCREMENT,' +
                   'setting_name TEXT,setting_value TEXT)')
    connection_obj.close()


def get_setting_value(setting_name):
    """
    | This function returns the value of specific setting .
    :param setting_name str
    :return str
    """
    connection_obj = connect_db()
    cursor = connection_obj.cursor()
    execute = cursor.execute("SELECT setting_value FROM settings WHERE setting_name = '" + setting_name + "'")
    setting_value = execute.fetchall()
    connection_obj.close()
    try:
        return setting_value[0]
    except IndexError:
        return ""


def set_setting(setting_name_string, setting_value_string):
    """
    | This function sets a setting name and value.If that setting_name exists, updates it's value, Otherwise
    | Insert that to the table
    :param setting_name str
    :param setting_value str
    """
    connection_obj = connect_db()
    cursor = connection_obj.cursor()
    if get_setting_value(setting_name_string):
        cursor.execute("UPDATE settings SET setting_value = '" +setting_value_string + "' WHERE setting_name = '" + setting_name_string +"'")
        cursor.commit()
    else:
        cursor.executemany('INSERT INTO settings VALUES (?,?)', ((setting_name_string, setting_value_string),))
        cursor.commit()
    connection_obj.close()