from sqlite3 import *


def connect_db():
    """
    | This function make a connection to the userDatabase database and returns that;
    :return :sqlite3 connection object
    """
    return connect('userDatabase.db')


def create_settings_table():
    """
    | This void function creates users table if it not exists.
    create_users_table()
    """
    connection_obj = connect_db()
    cursor = connection_obj.cursor()
    connection_obj.commit()
    cursor.execute('CREATE TABLE IF NOT EXISTS settings(id INTEGER PRIMARY KEY,' +
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
    with connection_obj:
        cursor = connection_obj.cursor()
        last_id = cursor.lastrowid
        if get_setting_value(setting_name_string):
            cursor.execute("UPDATE settings SET setting_value = '" +setting_value_string + "' WHERE setting_name = '" + setting_name_string +"'")
        else:
            row_ids = cursor.execute('SELECT id FROM settings')
            row_ids = row_ids.fetchall()
            print row_ids
            row_id = max([id_num[0] for id_num in row_ids]) + 1
            print 'kir'
            print setting_name_string
            print setting_value_string
            print row_id
            print type(setting_name_string)
            print type(setting_value_string)
            print type(row_id)
            cursor.executemany('INSERT INTO settings(setting_name, setting_value) VALUES (?,?)', ((setting_name_string, setting_value_string),))
        print cursor.execute('SELECT * FROM settings').fetchall()
