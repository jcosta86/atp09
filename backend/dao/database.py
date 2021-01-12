import psycopg2

host = 'pgsql08-farm15.uni5.net'
user = 'topskills10'
password = 'olist123'
database = 'topskills10'


def execute_query(query: str) -> None: #Function for use with insert and create query
    connection_string = f"host={host} user={user} dbname={database} password={password}"
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()


def select_query(query: str) -> list: #Function for return values (Use with select)
    connection_string = f"host={host} user={user} dbname={database} password={password}"
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    
    return result