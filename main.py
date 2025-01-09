from pyproj import Transformer
from pyproj import CRS

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
    wgs84_coordinates = convert_nad83_to_wgs84(nad83_easting, nad83_northing)
    print(f"NAD83 Coordinates: Easting = {nad83_easting}, Northing = {nad83_northing}")
    print(f"WGS84 Coordinates: Longitude = {wgs84_coordinates[0]}, Latitude = {wgs84_coordinates[1]}")


