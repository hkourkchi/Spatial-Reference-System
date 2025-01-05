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
   python main.py
   ```

5. The script will output the corresponding WGS84 coordinates (longitude, latitude).
```


