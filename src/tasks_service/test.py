import psycopg2
 
# try:
#     conn = psycopg2.connect(dbname='tasks_db', user='tasks_service_login', password='megapassword52fortasksservice', host='0.0.0.0', port='8093')
# except Exception as e:
#     print(e)
#     print('Can`t establish connection to database')
 
# with conn.cursor() as cursor:
#     cursor.execute(f"CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT)")
#     cursor.execute(f"INSERT INTO test (id, name) VALUES (123, 'maks')")
#     cursor.execute(f"REPLACE INTO test (id, name) VALUES (123, 'makson')")
#     cursor.execute("SELECT * FROM test")
#     res = cursor.fetchall()
 
# print(res)

# conn.close()

from os import path
d = path.dirname(path.abspath(__file__))
print(d)
print(type(d))
# print(path.dirname(d))