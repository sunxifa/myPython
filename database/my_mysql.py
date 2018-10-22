import mysql.connector
from python_mysql_connect1 import connect


# conn = mysql.connector.connect(host='192.168.179.134', port='32768', user='root',
# password='123456a?', database='test01', use_unicode=True)
conn = connect()

cursor = conn.cursor()
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))

# conn.commit()
# cursor.close()

cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print values
cursor.close()
conn.close()
