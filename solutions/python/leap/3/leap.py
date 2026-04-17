def leap_year(year):
    """Function returning bool whether a given year is a leap year."""
    if year % 4 == 0 and year % 400 == 0:
        return True
    if year % 4 == 0 and not year % 100 == 0:
        return True
    return False