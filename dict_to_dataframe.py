import re
import datetime
import pandas as pd

def translate_date(string):
    """
    Translate owl represented time to datetime now time
    @param string:
    @return:
    """
    string = re.split(r"[,\s]+", string)
    string[3] = string[3] + ':00'

    # adjust to military time
    if string[4] == "PM":
        time = string[3].split(":")
        time[0] = str(int(time[0]) + 12)
        string[3] = ":".join(time)

    string[0] = convert_month(string[0])
    return string[2] + "-" + string[0] + "-" + string[1], string[3]


def convert_month(month):
    dic = {"Jan": "01", "Fed": "02", "Mar": "03",
           "Apr": "04", "May": "05", "Jun": "06",
           "Jul": "07", "Aug": "08", "Sep": "09",
           "Oct": "10", "Nov": "11", "Dec": "12"}
    return dic[month]

def change_to_df(data):
    # Turn each course in the dictionary to a dataframe
    dfs = []
    for key in data:
        course = pd.DataFrame(data[key], index=['Course', 'Status', 'Open Date', 'Due Date']).T
        dfs.append(course)

    for df in dfs:
        for index, row in df.iterrows():
            if row['Due Date'] != '':
                row['Due Date'] = translate_date(row['Due Date'])
            row['Open Date'] = translate_date(row['Open Date'])
    return dfs