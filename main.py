
from Scraper     import Scraper
from Parser      import Parser
from os          import environ
from datetime    import datetime
from AzureClient import AzureClient
from json        import dumps       as dump_string
from time        import sleep

#  TODO :
#    - Notifiaction System
#    - Logging System

def get_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":

    # Declaring Managers
    sc = Scraper("weather.log", "countries2.json", 2)
    pr = Parser("weather.log")
    ac = AzureClient(environ.get("AZURE_DB_SECRET"))

    sc.load_data()

    while True:

        # Scape Data
        print("SCRAPING DATA:")
        sc.start()

        # Parse The Scraped Data
        print("PARSING DATA:")
        temp_dict, temp_rel, avg = pr.parse()

        # Save the data to the Azure SQL B
        print("PUSHING TO DB:")
        command = f"('{get_date()}',{avg},'{dump_string(temp_dict)}','{dump_string(temp_rel)}')"
        ac.exec_push(command)

        # Clear weather.log for next iteration
        print("CLEARING LOG:")
        tmp = open("weather.log", "w")
        tmp.close()


        # Repeat every 1/4th of a day
        # sleep(21600)
        break