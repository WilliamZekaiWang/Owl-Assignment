from bs4 import BeautifulSoup
import requests
from scraper import *
from dict_to_dataframe import *
import datetime
from datetime import datetime
import pandas as pd


def main():
    current_day = str(datetime.now())[:19]
    print(f"The current date and time is: {current_day}")
    current_day = current_day.split(" ")

    dfs = change_to_df(login())
    print(dfs)
    # Change each date from owl's format into one compatible with datetime




if __name__ == "__main__":
    main()
