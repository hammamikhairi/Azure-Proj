from pyodbc import connect


class AzureClient:
    USERNAME    : str = "YOUR_USERNAME"
    DATABASE    : str = "YOUR_DATABASE_NAME"
    SERVER      : str = "YOUR_SERVER_NAME"
    PORT        : str = 1433

    DRIVER      : str = '{ODBC Driver 17 for SQL Server}'
    TABLE_NAME  : str = "COUNTRIES_TABLE"
    SERVER_LINK : str

    def __init__(self, pwd : str):
        self.SERVER_LINK : str =  f'DRIVER={self.DRIVER};SERVER=tcp:{self.SERVER};PORT={self.PORT};DATABASE={self.DATABASE};UID={self.USERNAME};PWD={pwd}'

    def exec_push(self, values):
        with connect(self.SERVER_LINK) as conn:
            with conn.cursor() as cursor:
                query = f"""INSERT INTO {self.TABLE_NAME} (COUNTRY, CAPITAL) VALUES {values};"""
                cursor.execute(query)
        print("Pushed Data to DB.")

    def exec_get(self, query):
        with connect(self.SERVER_LINK) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                row = cursor.fetchone()
                while row:
                    yield row
                    row = cursor.fetchone()
