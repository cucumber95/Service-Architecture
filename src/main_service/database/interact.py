import sqlite3

def execute_query(connection, query):
    connection.cursor().execute(query)
    connection.commit()

def execute_read_query(connection, query):
    cursor = connection.cursor().execute(query)
    return cursor.fetchall()


def create_table(connection, name, columns):
    query = f"CREATE TABLE IF NOT EXISTS {name} ({columns});"
    execute_query(connection, query)

def insert_row(connection, table_name, row):
    query = f"REPLACE INTO {table_name} VALUES ({row})"
    execute_query(connection, query)

def insert_empty_row(connection, table_name, key_name, key):
    query = f"REPLACE INTO {table_name} ({key_name}) VALUES ({key})"
    execute_query(connection, query)

def update_row(connection, table_name, key_name, key, column, value):
    query = f"UPDATE {table_name} SET {column} = {value} WHERE {key_name} = {key}"
    execute_query(connection, query)

def get_row(connection, table_name, key_name, key):
    query = f"SELECT * FROM {table_name} WHERE {key_name} = {key}"
    return execute_read_query(connection, query)
    
    
def create_connection():
    return sqlite3.connect("database.db", check_same_thread=False)