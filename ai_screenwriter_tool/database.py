```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:') # creates a database in RAM
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def close_connection(conn):
    conn.close()

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"ai_screenwriter_tool.db"

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        email text NOT NULL UNIQUE,
                                        password text NOT NULL,
                                        subscription text,
                                        tokens integer
                                    ); """

    sql_create_projects_table = """CREATE TABLE IF NOT EXISTS projects (
                                    id integer PRIMARY KEY,
                                    user_id integer NOT NULL,
                                    title text NOT NULL,
                                    screenplay text NOT NULL,
                                    FOREIGN KEY (user_id) REFERENCES users (id)
                                );"""

    sql_create_tokens_table = """ CREATE TABLE IF NOT EXISTS tokens (
                                        id integer PRIMARY KEY,
                                        user_id integer NOT NULL,
                                        token_count integer NOT NULL,
                                        FOREIGN KEY (user_id) REFERENCES users (id)
                                    ); """

    sql_create_subscriptions_table = """ CREATE TABLE IF NOT EXISTS subscriptions (
                                            id integer PRIMARY KEY,
                                            user_id integer NOT NULL,
                                            subscription_type text NOT NULL,
                                            FOREIGN KEY (user_id) REFERENCES users (id)
                                        ); """

    conn = create_connection()

    if conn is not None:
        create_table(conn, sql_create_users_table)
        create_table(conn, sql_create_projects_table)
        create_table(conn, sql_create_tokens_table)
        create_table(conn, sql_create_subscriptions_table)
    else:
        print("Error! cannot create the database connection.")

    close_connection(conn)

if __name__ == '__main__':
    main()
```