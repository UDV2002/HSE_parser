import psycopg2
from db_config import host, user, password, db_name
from rich import print as rprint


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
        rprint('[italic green][INFO] Connection to database successful[/italic green]\n')
        with conn.cursor() as c:
            c.execute(
                f"""CREATE TABLE IF NOT EXISTS {table_name}(
                {parameters})"""
            )

        conn.commit()
        rprint(f'[italic green][INFO] table {table_name} created successfully[/italic green]\n')

    except Exception as e:
        rprint('[italic red][INFO] Error while working with PostgreSQL[/italic red]', e, "\n")

    finally:
        if conn:
            conn.close()
            rprint('[italic green][INFO] PostgreSQL connection closed[/italic green]')


def insert_into_table(table_name, columns, values_amount, values):
    try:
        conn = db_connection()
        rprint("[italic green][INFO] Connection to database successful[/italic green]\n")
        with conn.cursor() as c:
            c.execute(f"""INSERT INTO {table_name} ({columns}) VALUES {values};""")
        conn.commit()
        rprint(f'[italic green][INFO] Successfully inserted data into {table_name} table[/italic green]\n')

    except Exception as e:
        rprint(f"[italic red][INFO] Error while trying to insert data to {table_name} table[/italic red]", e, "\n")

    finally:
        if conn:
            conn.close()


def print_table_data(data, table_name, condition):
    try:
        conn = db_connection()
        rprint("[italic green][INFO] Connection to database successful[/italic green]\n")

        with conn.cursor() as c:
            c.execute(f"""SELECT {data} FROM {table_name} {condition};""")
            for line in c.fetchall():
                print(line)

        rprint(f'[italic green][INFO] Successfully selected data from {table_name} table[/italic green]\n')

    except Exception as e:
        rprint(f"[italic red][INFO] Error while trying to select data from {table_name} table[/italic red]", e, "\n")

    finally:
        if conn:
            conn.close()
