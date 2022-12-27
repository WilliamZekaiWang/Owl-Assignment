from datetime import datetime

def days_away(current, assignment):
    return str(datetime.strptime(assignment, "%Y-%m-%d") - datetime.strptime(current, "%Y-%m-%d"))

def hours_away(current, assignment):
    return str(datetime.strptime(assignment, "%H:%M:%S") - datetime.strptime(current, "%H:%M:%S"))