import mysql.connector
from mysql.connector import Error
from python_mysql_dbconfig import read_db_config


def connect():
    ''' Connect to MySQL database '''

    db_config = read_db_config()

    try:
        print('Connecting to MySQL database...')
        conn = mysql.connector.connect(**db_config)

        if conn.is_connected():
            print('connection established.')
        else:
            print ('connection failed.')

    except Error as error:
        print(error)
    # finally:
        # conn.close()
        # print('Connection closed.')
    return conn


if __name__ == '__main__':
    connect()
