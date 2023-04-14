from datetime import datetime
from controllers.Notes_control import int_check


def year_check(year):
    check = False
    while not check:
        if int_check(year):
            year = int(year)
            if year < 0 or year > datetime.now().year:
                year = input("Wrong year! Try again: ")
        else:
            return year_check(input("Not a number! Try again: "))
        check = True
    return year


def month_check(month):
    check = False
    while not check:
        if int_check(month):
            month = int(month)
            if month < 0 or month > 12:
                month = input("Wrong month! Try again: ")
        else:
            return month_check(input("Not a number! Try again: "))
        check = True
    return month


def day_check(day):
    check = False
    while not check:
        if int_check(day):
            day = int(day)
            if day < 0 or day > 31:
                day = input("Wrong day! Try again: ")
        else:
            return day_check(input("Not a number! Try again: "))
        check = True
    return day


def hour_check(hour):
    check = False
    while not check:
        if int_check(hour):
            hour = int(hour)
            if hour < 0 or hour >= 24:
                hour = input("Wrong hour! Try again: ")
        else:
            return hour_check(input("Not a number! Try again: "))
        check = True
    return hour


def minute_check(minute):
    check = False
    while not check:
        if int_check(minute):
            minute = int(minute)
            if minute < 0 or minute > 59:
                minute = input("Wrong minute! Try again: ")
        else:
            return minute_check(input("Not a number! Try again: "))
        check = True
    return minute


def date_time_select():
    pattern = '%Y %m %d %H %M'

    year = year_check(input("Input a year: "))
    month = month_check(input("Input a month: "))
    day = day_check(input("Input a day: "))
    hour = hour_check(input("Input a hour: "))
    minute = minute_check(input("Input a minute: "))

    check_str = f"{year} {month} {day} {hour} {minute}"
    try:
        date_time = datetime.strptime(check_str, pattern)
    except ValueError:
        print("Wrong date! Try again!")
        return date_time_select()
    return date_time


def select_date_range():
    print("Input a start date.")
    start_date = date_time_select()

    print("\nInput a end date.")
    end_date = date_time_select()

    return start_date, end_date
