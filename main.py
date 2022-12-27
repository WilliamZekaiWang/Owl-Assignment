from scraper import *
from dict_to_dataframe import *
import datetime
from datetime import datetime
from utils import *

def main():
    # Get current day details to be able to compare to owl assignments
    current_day = str(datetime.now())[:19]
    print(f"The current date and time is: {current_day}")
    current_day = current_day.split(" ")

    # get data from owl and analyze the df to see which assignments are upcoming
    dfs = change_to_df(login())
    for df in dfs:
        todo = {'Within 7 Days': {},
                'Greater Than 7 Days': {},
                'Today': {}
                }
        for index, assignment in enumerate(list(df.index.values)):
            if df['Due Date'][index] != "":
                days = int(days_away(current_day[0], df['Due Date'][index][0]).split(" ")[0])
                if days == 0:
                    todo['Today'].update({assignment: (hours_away(current_day[1], df['Due Date'][index][1])) + "Hours"})
                elif 0 <= days <= 7:
                    todo['Within 7 Days'].update({assignment: str(days) + " Days"})
                elif days > 7:
                    todo['Greater Than 7 Days'].update({assignment: str(days) + " Days"})
                else:
                    break

    display_assignments(todo)

def display_assignments(dic):

    for key, value in dic.items():
        if value:
            print(f"{key}:")
            for assignment, time in value.items():
                print(f"   {assignment}: due in {time}")

if __name__ == "__main__":
    main()
