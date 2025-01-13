import unittest
import pandas as pd
from main import convert_nad83_to_wgs84

class convert_nad83_to_wgs84_unit_test(unittest.TestCase):
    def test_convert_nad83_to_wgs84_precision_place_5(self):
        file_path_validation = 'validation_nad83_wgs84.csv'
        df_val = pd.read_csv(file_path_validation)
        for index, row in df_val.iterrows():
            long_out, lat_out = convert_nad83_to_wgs84(row.nad83_easting, row.nad83_northing)
            self.assertAlmostEqual(long_out, row.wgs84_longitude, 5,f"Error in longitude conversion in row : {index}")
            self.assertAlmostEqual(lat_out, row.wgs84_latitude,  5,f"Mismatch in latitude conversion in row : {index}")
    def test_convert_nad83_to_wgs84_precision_place_6(self):
        file_path_validation = 'validation_nad83_wgs84.csv'
        df_val = pd.read_csv(file_path_validation)
        for index, row in df_val.iterrows():
            long_out, lat_out = convert_nad83_to_wgs84(row.nad83_easting, row.nad83_northing)
            self.assertAlmostEqual(long_out, row.wgs84_longitude, 6,f"Error in longitude conversion in row : {index}")
            self.assertAlmostEqual(lat_out, row.wgs84_latitude,  6,f"Mismatch in latitude conversion in row : {index}")
if __name__ == '__main__':
    unittest.main()
