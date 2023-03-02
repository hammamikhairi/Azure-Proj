
from pyodbc import connect


class AzureClient:
    DRIVER      : str = '{ODBC Driver 17 for SQL Server}'
    USERNAME    : str = "khairi"
    DATABASE    : str = "stal"
    SERVER      : str = "stal-server.database.windows.net"
    PORT        : str = "1433"
    TABLE_NAME  : str = "ScrapingData"

    SERVER_LINK : str

    def __init__(self, pwd : str):
        self.SERVER_LINK : str =  f'DRIVER={self.DRIVER};SERVER=tcp:{self.SERVER};PORT={self.PORT};DATABASE={self.DATABASE};UID={self.USERNAME};PWD={pwd}'

    def exec_push(self, values):
        with connect(self.SERVER_LINK) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"""INSERT INTO {self.TABLE_NAME} (date, avg, data, count_avg) VALUES {values};""")

    # returns tuples
    def exec_get(self, query):
        with connect(self.SERVER_LINK) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                row = cursor.fetchone()
                while row:
                    yield row
                    row = cursor.fetchone()


