"""
This is a unit test for convert_nad83_to_wgs84 function
"""

import unittest
import pandas as pd
from convertor_csv import convert_nad83_to_wgs84


class ConvertNad83ToWgs84UnitTest(unittest.TestCase):
    """
    This is a unit test for convert_nad83_to_wgs84 function
    """
    def test_convert_nad83_to_wgs84_precision_place_5(self):
        """
        Verifies the output precision up to 5 decimal places
        """
        file_path_validation = 'validation_nad83_wgs84.csv'
        df_val = pd.read_csv(file_path_validation)
        for index, row in df_val.iterrows():
            long_out, lat_out = convert_nad83_to_wgs84(row.nad83_easting, row.nad83_northing)
            self.assertAlmostEqual(long_out, row.wgs84_longitude, 5,
                                   f"Error in longitude conversion in row : {index}")
            self.assertAlmostEqual(lat_out, row.wgs84_latitude, 5,
                                   f"Mismatch in latitude conversion in row : {index}")

    def test_convert_nad83_to_wgs84_precision_place_6(self):
        """
        Verifies the output precision up to 6 decimal places
        """
        file_path_validation = 'validation_nad83_wgs84.csv'
        df_val = pd.read_csv(file_path_validation)
        for index, row in df_val.iterrows():
            long_out, lat_out = convert_nad83_to_wgs84(row.nad83_easting, row.nad83_northing)
            self.assertAlmostEqual(long_out, row.wgs84_longitude, 6,
                                   f"Error in longitude conversion in row : {index}")
            self.assertAlmostEqual(lat_out, row.wgs84_latitude, 6,
                                   f"Mismatch in latitude conversion in row : {index}")


if __name__ == '__main__':
    unittest.main()
