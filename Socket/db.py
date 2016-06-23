import MySQLdb as m
from _config import DBHOST, DBNAME, DBPASS, DBUSER


def connection():
    return m.Connection(DBHOST, DBUSER, DBPASS, DBNAME)


def create_settings_table():
    """
    | This void function creates users table if it not exists.
    create_users_table()
    """
    connection_obj = connection()
    cursor = connection_obj.cursor()
    connection_obj.commit()
    cursor.execute('CREATE TABLE IF NOT EXISTS settings(id INT PRIMARY KEY AUTO_INCREMENT,' +
                   'setting_name VARCHAR(255),setting_value VARCHAR(255))')
    connection_obj.close()


def get_setting_value(setting_name):
    """
    | This function returns the value of specific setting .
    :param setting_name str
    :return str
    """
    connection_obj = connection()
    cursor = connection_obj.cursor()
    cursor.execute("SELECT setting_value FROM settings WHERE setting_name = %s", (setting_name,))
    setting_value = cursor.fetchone()
    try:
        return setting_value[0]
    except IndexError:
        return ""
    except TypeError as e:
        print e
        return ""


def set_setting(setting_name_string, setting_value_string):
    """
    | This function sets a setting name and value.If that setting_name exists, updates it's value, Otherwise
    | Insert that to the table
    :param setting_name_string :str
    :param setting_value_string :str
    """
    connection_obj = connection()
    cursor = connection_obj.cursor()
    if get_setting_value(setting_name_string):
        cursor.execute("UPDATE settings SET setting_value = %s WHERE setting_name = %s", (setting_value_string,
                                                                                          setting_name_string))
        connection_obj.commit()
        return True
    else:
        cursor.execute('INSERT INTO settings VALUES (%s,%s)', (setting_name_string, setting_value_string))
        connection_obj.commit()
        return True
