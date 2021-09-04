from pyproj import CRS
crs_info = CRS.from_epsg(20936)
print(crs_info.to_wkt(pretty=True))