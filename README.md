# Coordinate Conversion Tool

This Python script converts coordinates between different coordinate systems. Currently, it supports conversion from NAD83 UTM (MTM Zone 8) to WGS84. Other conversions will be added in future updates.

## Description

The script uses the `pyproj` library to transform coordinates between different coordinate systems. It takes easting and northing values in NAD83 and outputs the corresponding longitude and latitude values in WGS84.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hkourkchi/Spatial-Reference-System
   cd <repository-directory>
   ```
   
2. Install the required dependencies:
   ```bash
   pip install pyproj
   ```

3. Update the `nad83_easting` and `nad83_northing` variables in the script with the coordinates you want to convert.
   
4. Run the script:
   ```bash
   python convertor_csv.py
   ```

5. The script will output the corresponding WGS84 coordinates (longitude, latitude).


## to use compiled exe file

1. Copy your `input_ad83.csv` file to the folder containing main.exe file (located in dist folder).

2. Run the convertor_csv.exe file to generate output file naming output_wgs84.csv.

3. To generate the exe file type `pyinstaller convertor_csv.py` in terminal. Note that you 
   should install pyinstaller in advance. If it is not installed type `pip install pyinstaller` 
   in the terminal to install it.

## Pylint is added to the repo



