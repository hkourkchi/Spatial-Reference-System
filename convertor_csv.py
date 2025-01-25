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

    :param: nad83_easting (float): Easting in NAD83 MTM Zone 8
    :param: nad83_northing (float): Northing in NAD83 MTM Zone 8

    :return: tuple (longitude, latitude) : in WGS84
    """

    nad83_mtm = CRS.from_string("EPSG:2950")
    wgs84 = CRS.from_string("EPSG:4326")

    # Create a transformer object
    transformer = Transformer.from_crs(nad83_mtm, wgs84, always_xy=True)

    # Perform the transformation to WGS84
    longitude, latitude = transformer.transform(nad83_easting_in, nad83_northing_in)

    return longitude, latitude


def convert_csv_nad83_to_wgs84(file_path_in='input_nad83.csv', file_path_out='output_wgs84.csv'):
    """
    convert csv file of nad83 data points to wgs84 and save it
    :param: file_path_in (string): path to input file
    :param: file_path_out  (string): path to output file
    :return: NA
    """

    file_data_in = pd.read_csv(file_path_in)
    print(file_data_in.head())

    file_data_out = pd.DataFrame(np.zeros(file_data_in.shape),
                                 columns=['wgs84_longitude', 'wgs84_latitude'])
    for index, row in file_data_in.iterrows():
        # longitude, latitude = convert_nad83_to_wgs84(row.nad83_easting, row.nad83_northing)

        file_data_out.iloc[index] = convert_nad83_to_wgs84(row.nad83_easting, row.nad83_northing)
    print(file_data_out.head())

    # Check if the file already exists
    if os.path.exists(file_path_out):
        overwrite = input(
            f"The file {file_path_out} already exists. Do you want to overwrite it? (Y/N): ")
        if overwrite.lower() == 'y':
            # Save the DataFrame to a CSV file
            with open(file_path_out, 'w', encoding='str', newline='') as file:
                file_data_out.to_csv(file, index=False)
            print(f"The file has been overwritten and saved to {file_path_out}.")
        else:
            print("The file was not overwritten.")
    else:
        # Save the DataFrame to a CSV file
        file_data_out.to_csv(file_path_out, index=False)
        print(f"The file has been saved to {file_path_out}.")


if __name__ == '__main__':
    continue_flag: str = 'Y'

    while continue_flag.upper() == 'Y':
        print('This is to convert csv file of NAD83 data to WGS84 csv file')
        print('The default input/output files: input_nad83.csv wgs84_latitude')

        rename_flag = input('Do you want to rename them? (Y/N)')
        if rename_flag.upper() == 'Y':
            in_file_name = input('Enter your input csv file name')
            out_file_name = input('Enter your output csv file name')
            try:
                convert_csv_nad83_to_wgs84(in_file_name, out_file_name)
            except Exception as e: # pylint: disable=broad-except
                print(f"An error occurred: {e}")
        else:
            try:
                convert_csv_nad83_to_wgs84()
            except Exception as e: # pylint: disable=broad-except
                print(f"An error occurred: {e}")
        continue_flag = input('Do you want another conversion? (Y/N)')
