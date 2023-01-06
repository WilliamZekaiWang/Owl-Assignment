from scraper import *
from dict_to_dataframe import *
import datetime
from utils import *

def owl_assignments():
    # Get current day details to be able to compare to owl assignments
    current_day = str(datetime.now())[:19]
    print(f"The current date and time is: {current_day}")
    current_day = current_day.split(" ")

    # get data from owl and analyze the df to see which assignments are upcoming
    dfs = change_to_df(login())
    todo = {'Today': {},
            'Within 7 Days': {},
            'Greater Than 7 Days': {}
            }
    for df in dfs:
        for index, assignment in enumerate(list(df.index.values)):
            if df['Due Date'][index] != "":
                days = int(days_away(current_day[0], df['Due Date'][index][0]).split(" ")[0])
                if days == 0:
                    todo['Today'].update({assignment: ((hours_away(current_day[1], df['Due Date'][index][1])) + " Hour(s)", df['Course'][index])})
                elif 0 <= days <= 7:
                    todo['Within 7 Days'].update({assignment: (str(days) + " Day(s)", df['Course'][index])})
                elif days > 7:
                    todo['Greater Than 7 Days'].update({assignment: (str(days) + " Day(s)", df['Course'][index])})
                else:
                    break  # they should be sorted by date already so no need to check later dates
    display_assignments(todo)
    exit()

def display_assignments(dic):
    """
    displays on terminal the necessary information
    @param dic courses and assignment and prints them all pretty
    @return: void
    """
    print("Upcoming Assignments\n")
    for key, value in dic.items():
        if value:
            print("-"*100)
            print(f"{key}:")
            for assignment, info in value.items():
                print(f"   {info[1]}: {assignment}, due in {info[0]}")
            print("-" * 100)
        else:
            print(f"You have no assignments due {key}\n")

if __name__ == "__main__":
    owl_assignments()