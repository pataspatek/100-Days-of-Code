def leap_year(x):
    """Checks if a given year is a leap year or not."""
    if x % 4 == 0 and (x % 100 != 0 or x % 400 == 0):
        return True
    else:
        return False


def days_in_month(year, month):
    """Gives a number of days in a specific month and specific year. 
    Takes in count whether the year is leap or not."""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = month_days[month - 1]

    if leap_year(year):
        month = month_days[1] + 1
    return month


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)

print(days)