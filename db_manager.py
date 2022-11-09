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
        print('[INFO] Connection successful')
        with conn.cursor() as c:
            c.execute(
                f"""CREATE TABLE IF NOT EXISTS {table_name}(
                {parameters})"""
            )

        conn.commit()
        print(f'[INFO] table {table_name} created successfully')

    except Exception as e:
        print('[INFO] Error while working with PostgreSQL', e)

    finally:
        if conn:
            conn.close()
            print('[INFO] PostgreSQL connection closed')


def insert_into_table(table_name, columns, values_amount, values):
    try:
        conn = db_connection()
        print("[INFO] Connection successful")
        with conn.cursor() as c:
            c.execute(f"""INSERT INTO {table_name} ({columns}) VALUES {values};""")
        conn.commit()
        print(f'[INFO] Successfully inserted data into {table_name} table')

    except Exception as e:
        print(f"[INFO] Error while trying to insert data to {table_name} table", e)

    finally:
        if conn:
            conn.close()


# create_table("faculties", "id serial PRIMARY KEY,"
#                           "name varchar(100) NOT NULL,"
#                           "link varchar NOT NULL")

create_table("magister_courses", "id serial PRIMARY KEY,"
                                 "name varchar(100) NOT NULL,"
                                 "link varchar NOT NULL,"
                                 "language varchar(20) NOT NULL,"
                                 "campus varchar(20) NOT NULL,"
                                 "duration varchar(20) NOT NULL,"
                                 "places varchar,"
                                 "education_form varchar(20) NOT NULL")
