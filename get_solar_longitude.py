import datetime
from math import floor, ceil, sin


HOURS_IN_DAY = 24
CONVERT_CONST_FOR_GMAT = -12
JULIAN_DAY_FROM_EPOCH = 2440587 
'Used 01.01.1970 as epoch'
MAX_SUN_L = 360


def get_valid_hour_day_format(hour: int, day: int, value: int) -> tuple([int, int]):
    """
    Returns a valid hour, day format.
    Hour can be 0 to 23, day from 1 to 31;
    Value can be any integer number, but as default possible values are all gmt values.
    """
    if hour + value < 0:
        day -= 1
        hour = HOURS_IN_DAY + value + hour
    elif (hour + value) > HOURS_IN_DAY:
        day += 1
        hour = (hour + value) % 24
    else:
        hour += value
    return hour, day



def convert_to_ut(year: int, month: int, day: int, hour: int, minutes: int, gmt_value: int):
    """
    Converts a datetime to UT.
    """

    hour, day = get_valid_hour_day_format(hour, day, gmt_value)

    return datetime.datetime(year, month, day, hour, minutes)


def convert_to_gmat(year: int, month: int, day: int, hour: int, minutes: int, gmt_value: int):
    """
    Converts a datetime to GMAT (Greenwich Mean Astronomical Time).
    """
    ut_time = convert_to_ut(year, month, day, hour, minutes, gmt_value)
    gmat_hour, gmat_day = get_valid_hour_day_format(ut_time.hour, ut_time.day, value=CONVERT_CONST_FOR_GMAT)

    return datetime.datetime(year, month, gmat_day, gmat_hour, minutes)


def get_decimal_part_of_day(hours: int, minutes: int):
    return round(((hours + minutes / 60) / 24), 4)


def get_julian_day_number(year: int, month: int, day: int) -> int:
    """
    Returns the Julian day number of a given date.
    For more information, look at the https://en.wikipedia.org/wiki/Julian_day
    """
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3
    JDN = day  + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
    return JDN


def get_jd(year, month, day, hours, minutes, gmt_value):
    gmat_time = convert_to_gmat(year, month, day, hours, minutes, gmt_value)
    return get_julian_day_number(gmat_time.year, gmat_time.month, gmat_time.day) + get_decimal_part_of_day(gmat_time.hour, gmat_time.minute)


def calc_mean_longitude(jd: float) -> float:
    """
    Calculates the mean longitude of the Sun by given Julian day.
    Mean longitude is defined in range from 0 to 360.
    """
    L = 0
    secondary_value = 280.461 + 0.9856474 * jd
    if secondary_value > MAX_SUN_L:
        number = secondary_value // MAX_SUN_L
        L = secondary_value - number * MAX_SUN_L
    return round(L, 5)


def calc_mean_anomaly(jd: float) -> float:
    """
    Calculates the mean anomaly of the Sun by given Julian day.
    Mean anomaly is defined in range from 0 to 360.
    """
    g = 0
    secondary_value = 357.528 + 0.9856003 * jd
    if secondary_value > MAX_SUN_L:
        number = secondary_value // MAX_SUN_L
        g = secondary_value - number * MAX_SUN_L
    return round(g, 5)

def calc_solar_longitude(Ls: float, g: float) -> float:
    """
    Calculates the solar longitude of the Sun by given mean longitude and mean anomaly of Sun.
    Solar longitude is defined in range from 0 to 360.
    """
    return round(Ls + 1.915 * sin(g) + 0.02 * sin(2 * g), 5)
    