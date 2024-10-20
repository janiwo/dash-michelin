from typing import Dict, List
import geopandas as gpd

from shapely import Polygon, Point


class ViewPortHandler:

    def __init__(self, viewport: Dict) -> None:

        # TODO handling if viewport is None (for whatever reason)
        if viewport is None:
            self.center = dict(lat=20.0, lon=0.0)
            self.zoom = 1
            self.bearing = None
            self.pitch = None
            self.area = None

        else:

            self.center = dict(
                lat=viewport["map.center"]["lat"], lon=viewport["map.center"]["lon"]
            )

            self.zoom = viewport["map.zoom"]
            self.bearing = viewport["map.bearing"]
            self.pitch = viewport["map.pitch"]
            self.area = Polygon(viewport["map._derived"]["coordinates"])

    def get_coordinates_in_view(
        self, gs: gpd.GeoSeries, ids_only: bool = True
    ) -> List[int]:

        mask = gs.within(self.area)
        gs_filtered = gs[mask]

        if ids_only:
            return gs_filtered.index

        return gs_filtered
