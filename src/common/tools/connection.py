import pymysql
import config


class Connection:
    databases = None

    def __init__(self):
        self._conn = pymysql.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            port=int(config.DB_PORT),
            password=config.DB_PASSWORD,
            db=config.DB_NAME)
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    '''
        Non select statements
    '''

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

    def rows(self):
        return self.cursor.rowcount

    def description(self):
        return self.cursor.description