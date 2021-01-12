import psycopg2

host = 'pgsql08-farm15.uni5.net'
user = 'topskills10'
password = 'olist123'
database = 'topskills10'


def insert_query(query: str):
    connection_string = f"host={host} user={user} dbname={database} password={password}"
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute(query)
    print("Query executada")
    connection.commit()
    cursor.close()
    connection.close()


def select_query(query: str):
    connection_string = f"host={host} user={user} dbname={database} password={password}"
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    
    return result