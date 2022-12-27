from bs4 import BeautifulSoup
import requests
from scraper import *
from utils import *
import datetime
from datetime import datetime


def main():
    current_day = str(datetime.now())[:19]
    print(f"The current date and time is: {current_day}")
    current_day = current_day.split(" ")

    data = login()
    for course in data:
        for assignment in course:
            assignment[1] = assignment[1]

if __name__ == "__main__":
    main()
