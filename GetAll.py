from AzureClient import AzureClient
from os          import environ

if __name__ == "__main__" : 
    client = AzureClient(environ.get("AZURE_DB_SECRET"))

    print("{:>30} {:30}".format("COUNTRY", "CAPITAL"))
    for row in client.exec_get("SELECT * FROM COUNTRIES_TABLE"):
        print("{} => {}".format(*row))
