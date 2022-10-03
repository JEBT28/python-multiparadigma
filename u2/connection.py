import psycopg2 as pg
import sys


class connection:

    _dbname = ''
    _user = ''
    _password = ''
    _host = ''
    _port = ''
    _conn = None

    def __init__(self, dbname, user, password, host, port):
        self._dbname = dbname
        self._user = user
        self._password = password
        self._host = host
        self._port = port

    def connect(self):
        try:
            self._conn = pg.connect(
                dbname=self._dbname, user=self._user, password=self._password, host=self._host)
        except pg.Error as e:
            print(e)
            sys.exit(1)

    def close(self):
        self._conn.close()

    def get_connection(self):
        return self._conn

    def get_cursor(self):
        return self._conn.cursor()

    def commit(self):
        self._conn.commit()

    def rollback(self):
        self._conn.rollback()


if __name__ == '__main__':
    conn = connection('u2', 'u2', 'u2', 'localhost', '5432')
    conn.connect()
    cur = conn.get_cursor()
    cur.execute('select * from users')
    print(cur.fetchall())
    conn.close()

