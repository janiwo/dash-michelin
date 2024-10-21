from typing import Union
import pandas as pd
from shapely.geometry import Point, LineString, Polygon
from shapely.ops import transform
import pyproj
import geopandas as gpd

from data.objects.michelin_data.michelin import MichelinData


class AreaHandler:

    def __init__(self, geo_object: Union[Point, LineString], distance_m: int) -> None:
        """Initializes AreaHandler class.

        Args:
            geo_object (Union[Point, LineString]): The object around which the area should be calculated. Can be either
                Point or LineString.
            distance_m (int): The buffer area (in meters) around the geo_object.
        """

        self.geo_object = geo_object
        self.distance_m = distance_m
        self.buffer_area = self._get_area()

    def _get_area(self) -> Polygon:
        """Applies a buffer area of n meters around a geo_object and returns the resulting area as a polygon.

        Returns:
            Polygon: Polygon describing the buffer area.
        """

        # https://epsg.io/4326
        epsg_4326 = pyproj.CRS("EPSG:4326")
        # https://epsg.io/3395
        epsg_3395 = pyproj.CRS("EPSG:3395")

        # project object to 4495
        project = pyproj.Transformer.from_proj(epsg_4326, epsg_3395)
        geo_object_3395 = transform(project.transform, self.geo_object)

        # calculate polygon for buffer area
        buffer_polygon_3395 = geo_object_3395.buffer(self.distance_m)

        # project polygon back to 4326
        project = pyproj.Transformer.from_proj(epsg_3395, epsg_4326)
        buffer_polygon_4326 = transform(project.transform, buffer_polygon_3395)

        return buffer_polygon_4326

    def check_location_in_area(self, geo_objects: gpd.GeoSeries) -> pd.Series:
        """Checks for a series of geo_objects if they are contained in the buffer area.

        Args:
            geo_objects (gpd.GeoSeries): Series of geo_objects, which should be shapely Points.

        Returns:
            pd.Series: Series of bool values indicating whether the geo_object is contained in the
                buffer area.
        """

        return geo_objects.within(self.buffer_area)


if __name__ == "__main__":

    data = MichelinData()
    df = data.df

    point = Point(12.57, 55.67)  # CPH
    geo_area_point = AreaHandler(geo_object=point, distance_m=10000)

    contained_mask_point = geo_area_point.check_location_in_area(
        geo_objects=df.geometry
    )

    df_point = df.copy()
    df_point = df_point.loc[contained_mask_point, :]

    line = LineString(coordinates=[[10.0, 53.55], [11.58, 48.13]])  # HH -> M
    geo_area_line = AreaHandler(geo_object=line, distance_m=10000)

    contained_mask_line = geo_area_line.check_location_in_area(geo_objects=df.geometry)

    df_line = df.copy()
    df_line = df_line.loc[contained_mask_line, :]
