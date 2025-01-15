"""
This script converts coordinates from the NAD83 MTM Zone 8 projection system to the WGS84 system.
The script reads input coordinates from a CSV file, performs the transformation, and saves the
output as a new CSV file.

The script uses the `pyproj` library for coordinate transformation and `pandas` for CSV file
handling.
It also includes safeguards to prevent overwriting the output file unless explicitly allowed by the
user.

Usage:
    1. Prepare an input CSV file named `input_nad83.csv` with columns `nad83_easting` and
    `nad83_northing`.
    2. Run the script to generate an output CSV file named `output_wgs84.csv` containing
       `wgs84_longitude` and `wgs84_latitude`.
    3. If the output file already exists, the user will be prompted for confirmation before
    overwriting.

Requirements:
    - pyproj
    - pandas
    - numpy
"""

import os
from pyproj import Transformer
from pyproj import CRS
import pandas as pd
import numpy as np


def convert_nad83_to_wgs84(nad83_easting_in, nad83_northing_in):
    """
    Convert coordinates from NAD83 MTM Zone 8 to WGS84.

    Parameters:
    nad83_easting (float): Easting in NAD83 MTM Zone 8
    nad83_northing (float): Northing in NAD83 MTM Zone 8

    Returns:
    tuple: (longitude, latitude) in WGS84
    """

    nad83_mtm = CRS.from_string("EPSG:2950")
    wgs84 = CRS.from_string("EPSG:4326")

    # Create a transformer object
    transformer = Transformer.from_crs(nad83_mtm, wgs84, always_xy=True)

    # Perform the transformation to WGS84
    longitude, latitude = transformer.transform(nad83_easting_in, nad83_northing_in)

    return longitude, latitude


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # # Load the CSV file
    FILE_PATH_IN = 'input_nad83.csv'
    file_data_in = pd.read_csv(FILE_PATH_IN)
    print(file_data_in.head())

    file_data_out = pd.DataFrame(np.zeros(file_data_in.shape),
                                 columns=['wgs84_longitude', 'wgs84_latitude'])
    for index, row in file_data_in.iterrows():
        # longitude, latitude = convert_nad83_to_wgs84(row.nad83_easting, row.nad83_northing)

        file_data_out.iloc[index] = convert_nad83_to_wgs84(row.nad83_easting, row.nad83_northing)
    print(file_data_out.head())

    FILE_PATH_OUT = 'output_wgs84.csv'

    # Check if the file already exists
    if os.path.exists(FILE_PATH_OUT):
        overwrite = input(
            f"The file {FILE_PATH_OUT} already exists. Do you want to overwrite it? (y/n): ")
        if overwrite.lower() == 'y':
            # Save the DataFrame to a CSV file
            file_data_out.to_csv(FILE_PATH_OUT, index=False)
            print(f"The file has been overwritten and saved to {FILE_PATH_OUT}.")
        else:
            print("The file was not overwritten.")
    else:
        # Save the DataFrame to a CSV file
        file_data_out.to_csv(FILE_PATH_OUT, index=False)
        print(f"The file has been saved to {FILE_PATH_OUT}.")
