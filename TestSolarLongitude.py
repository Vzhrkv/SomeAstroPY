import unittest
import datetime

from time_convertation.get_solar_longitude import get_valid_hour_day_format, convert_to_gmat, convert_to_ut, get_decimal_part_of_day,\
    get_julian_day_number, get_jd, calc_mean_longitude, calc_mean_anomaly, calc_solar_longitude


class TestGetValidHourDayFormat(unittest.TestCase):

    def setUp(self):
        self.valid_format_hour_day = get_valid_hour_day_format

    def test_valid_hour_day_format(self):
        self.assertEqual(self.valid_format_hour_day(0, 15, -3), (21, 14))    
        self.assertEqual(self.valid_format_hour_day(23, 10, 3), (2, 11))    
        self.assertEqual(self.valid_format_hour_day(20, 3, 5), (1, 4))    
        self.assertEqual(self.valid_format_hour_day(3, 4, 5), (8, 4))    


class TestUTConvert(unittest.TestCase):
    def setUp(self):
        self.convert_to_ut = convert_to_ut

    def test_convert_to_ut(self):
        self.assertEqual(self.convert_to_ut(2010, 6, 3, 20, 34, 5), datetime.datetime(2010, 6, 4, 1, 34))
        self.assertEqual(self.convert_to_ut(2010, 6, 4, 3, 16, 5), datetime.datetime(2010, 6, 4, 8, 16))
        self.assertEqual(self.convert_to_ut(2010, 1, 10, 1, 15, -2), datetime.datetime(2010, 1, 9, 23, 15))


class TestGMATconvert(unittest.TestCase):
    def setUp(self):
        self.gmat_convertation = convert_to_gmat
    
    def test_gmat_conversion(self):
        self.assertEqual(self.gmat_convertation(2010, 6, 3, 20, 34, 5), datetime.datetime(2010, 6, 3, 13, 34))
        self.assertEqual(self.gmat_convertation(2010, 6, 4, 3, 16, 5), datetime.datetime(2010, 6, 3, 20, 16))
        self.assertEqual(self.gmat_convertation(2010, 1, 10, 1, 15, -2), datetime.datetime(2010, 1, 9, 11, 15))


class TestDecimalPartOfDay(unittest.TestCase):
    def setUp(self):
        self.decimal_part_of_day = get_decimal_part_of_day

    def test_decimal_part_of_day(self):
        self.assertEqual(self.decimal_part_of_day(13, 34), .5653)
        self.assertEqual(self.decimal_part_of_day(20, 16), .8444)
        self.assertEqual(self.decimal_part_of_day(11, 15), .4688)


class TestJDN(unittest.TestCase):
    def setUp(self):
        self.jdn = get_julian_day_number

    def test_jdn(self):
        self.assertEqual(self.jdn(2010, 6, 3), 2455351)
        self.assertEqual(self.jdn(1970, 1, 1), 2440588)
        self.assertEqual(self.jdn(2001, 1, 7), 2451917)
        self.assertEqual(self.jdn(2010, 1, 9), 2455206)


class TestJD(unittest.TestCase):
    def setUp(self):
        self.jd = get_jd
    
    def test_jdn(self):
        self.assertEqual(self.jd(2010, 6, 3, 20, 34, 5), 2455351.5653)
        self.assertEqual(self.jd(2010, 6, 4, 3, 16, 5), 2455351.8444)
        self.assertEqual(self.jd(2010, 1, 10, 1, 15, -2), 2455206.4688) 


class TestMeanL(unittest.TestCase):
    def setUp(self):
        self.mean_l = calc_mean_longitude

    def test_mean_l(self):
        self.assertEqual(self.mean_l(2455206.4688), 328.33344)
        self.assertEqual(self.mean_l(2455351.8444), 111.62252)


class TestMeanAnomaly(unittest.TestCase):
    def setUp(self):
        self.mean_g = calc_mean_anomaly

    def test_mean_l(self):
        self.assertEqual(self.mean_g(2455206.4688), 289.76021)
        self.assertEqual(self.mean_g(2455351.8444), 73.04245)


class TestSUnLongitude(unittest.TestCase):
    def setUp(self):
        self.sun_l = calc_solar_longitude

    def test_sun_l(self):
        self.assertEqual(self.sun_l(328.33344, 289.76021), 329.63564)
        self.assertEqual(self.sun_l(111.62252, 73.04245), 110.28784)


if __name__ == '__main__':
    unittest.main()
    