
'''
Created on Mon Mar 21 20:17
@author: Lauren Galicia

'''

def weekday(date):
    '''
    This program returns the day of the week of any given date
    according to either the Julian calendar or the Gregorian calendar (if after 1752).

    Sample dates:
    1066/10/14  = Saturday  (Battle of Hastings)
    1776/7/4    = Thursday  (US Independence)
    2024/2/29   = Thursday  (next leap day)
    2101/1/1    = Saturday  (start of next century)

    Parameters
    ----------
    date : STRING
        A date in the format of year/month/day.
    Returns
    -------
    weekday : STRING
        The day of the week the date lands on.
    '''
    year, month, day = date.split('/')
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    century = int(year[:-2])
    year_code = sum([int(n) for n in [year[-2:], int(year[-2:])/4]]) % len(week)
    year, month, day = [int(n) for n in [year, day, month]]
    month -= 1
    month_code = '033614625035'[month]
    Gregorian = year > 1752
    century_code = '6420'[century % 4] if Gregorian else (18 - century) % len(week)
    leap = -1 if month < 2 and Gregorian and year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 0
    return week[sum([int(n) for n in [century_code, year_code, month_code, day, leap]]) % len(week)]

if __name__ == "__main__":
    date = input('Enter a date (year/month/day): ')
    print(weekday(date))
