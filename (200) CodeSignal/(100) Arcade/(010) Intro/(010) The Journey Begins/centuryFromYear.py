'''
CodeSignal > Arcade > Intro > The Journey Begin > CenturyFromYear
Write a function that returns the sum of two numbers.

Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

Example

For year = 1905, the output should be
centuryFromYear(year) = 20;
For year = 1700, the output should be
centuryFromYear(year) = 17.
'''


def centuryFromYear(year):
    if year < 100:
        return 1
    if year > 1000:
        if str(year)[-2:] == "00":
            return int(str(year)[:2])
        else:
            return int(str(year)[:2]) + 1
    else:
        if str(year)[-2:] == "00":
            return int(str(year)[0])
        else:
            return int(str(year)[0]) + 1
