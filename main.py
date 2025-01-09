from pyproj import Transformer
from pyproj import CRS
import pandas as pd
import numpy as np
import os

def convert_nad83_to_wgs84(nad83_easting, nad83_northing):
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
    longitude, latitude = transformer.transform(nad83_easting, nad83_northing)

    return longitude, latitude

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nad83_easting = 305517.50  # Example easting in NAD83 MTM Zone 8
    nad83_northing = 5036303.10  # Example northing in NAD83 MTM Zone 8
    # # Load the CSV file
    file_path_in = 'input_nad83.csv'
    file_data_in = pd.read_csv(file_path_in)
    print(file_data_in.head())

    file_data_out = pd.DataFrame(np.zeros(file_data_in.shape), columns=['wgs84_longitude', 'wgs84_latitude'])
    for index, row in file_data_in.iterrows():
        # longitude, latitude = convert_nad83_to_wgs84(row.nad83_easting, row.nad83_northing)

        file_data_out.iloc[index] = convert_nad83_to_wgs84(row.nad83_easting, row.nad83_northing)
    print(file_data_out.head())

    file_path_out = 'output_wgs84.csv'

    # Check if the file already exists
    if os.path.exists(file_path_out):
        overwrite = input(f"The file {file_path_out} already exists. Do you want to overwrite it? (y/n): ")
        if overwrite.lower() == 'y':
            # Save the DataFrame to a CSV file
            file_data_out.to_csv(file_path_out, index=False)
            print(f"The file has been overwritten and saved to {file_path_out}.")
        else:
            print("The file was not overwritten.")
    else:
        # Save the DataFrame to a CSV file
        file_data_out.to_csv(file_path_out, index=False)
        print(f"The file has been saved to {file_path_out}.")