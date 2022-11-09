import psycopg2
from db_config import host, user, password, db_name


def db_connection():
    return psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )


def create_table(table_name, parameters):
    try:
        conn = db_connection()
        print('[INFO] Connection successful\n')
        with conn.cursor() as c:
            c.execute(
                f"""CREATE TABLE IF NOT EXISTS {table_name}(
                {parameters})"""
            )

        conn.commit()
        print(f'[INFO] table {table_name} created successfully\n')

    except Exception as e:
        print('[INFO] Error while working with PostgreSQL', e, "\n")

    finally:
        if conn:
            conn.close()
            print('[INFO] PostgreSQL connection closed')


def insert_into_table(table_name, columns, values_amount, values):
    try:
        conn = db_connection()
        print("[INFO] Connection successful\n")
        with conn.cursor() as c:
            c.execute(f"""INSERT INTO {table_name} ({columns}) VALUES {values};""")
        conn.commit()
        print(f'[INFO] Successfully inserted data into {table_name} table\n')

    except Exception as e:
        print(f"[INFO] Error while trying to insert data to {table_name} table", e, "\n")

    finally:
        if conn:
            conn.close()


def print_table_data(data, table_name, condition):
    try:
        conn = db_connection()
        print("[INFO] Connection successful\n")

        with conn.cursor() as c:
            c.execute(f"""SELECT {data} FROM {table_name} {condition};""")
            print(c.fetchall())

        print(f'[INFO] Successfully selected data from {table_name} table\n')

    except Exception as e:
        print(f"[INFO] Error while trying to select data from {table_name} table", e, "\n")

    finally:
        if conn:
            conn.close()


