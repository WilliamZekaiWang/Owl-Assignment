from datetime import datetime

def days_away(current, assignment):
    """
    calculates current day and assignments if the days away from current day is greater one
    @param current: current day in Y-M-D
    @param assignment: the date of the assingment in Y-M-D
    @return: The amount of days left in a string from datetime strip
    """
    return str(datetime.strptime(assignment, "%Y-%m-%d") - datetime.strptime(current, "%Y-%m-%d"))

def hours_away(current, assignment):
    """
    calculates current time and assignments if the days away from current day is the due date
    @param current: current day in Y-M-D
    @param assignment: the date of the assingment in Y-M-D
    @return: the amount of horus left from date time
    """
    return str(datetime.strptime(assignment, "%H:%M:%S") - datetime.strptime(current, "%H:%M:%S"))