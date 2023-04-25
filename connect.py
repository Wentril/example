import psycopg2

from db_config import get_db_config


conn = psycopg2.connect(**get_db_config())


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    ret = ""
    try:
        # read connection parameters
        params = get_db_config()

        # connect to the PostgreSQL server
        ret += 'Connecting to the PostgreSQL database...\n'
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        ret += 'PostgreSQL database version: '
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        ret += str(db_version) + '\n'
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        ret += str(error) + '\n'
        print(error)
    finally:
        if conn is not None:
            conn.close()
            ret += 'Database connection closed.\n'
            print('Database connection closed.')

    return ret


if __name__ == '__main__':
    connect()
