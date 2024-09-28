from dataclasses import dataclass, field
import os
from typing import Optional
from decouple import config
import pandas as pd


@dataclass(frozen=True)
class MichelinRawColumns:
    name: str = "Name"
    address: str = "Address"
    location: str = "Location"
    price: str = "Price"
    cuisine: str = "Cuisine"
    longitude: str = "Longitude"
    latitude: str = "Latitude"
    phone_number: str = "PhoneNumber"
    michelin_url: str = "Url"
    website_url: str = "WebsiteUrl"
    award: str = "Award"
    has_green_star: str = "GreenStar"
    facilities_and_services: str = "FacilitiesAndServices"
    description: str = "Description"


@dataclass
class MichelinDataRaw:
    df: Optional[pd.DataFrame] = field(default=None)
    columns: MichelinRawColumns = MichelinRawColumns()
    path: Optional[str] = os.path.join(config("DATA_VAULT_PATH"), "michelin_raw.csv")

    def __post_init__(self):

        if self.df is None:

            self.df = self.load_data(self.path)

    def load_data(self, path: str) -> pd.DataFrame:

        return pd.read_csv(path)
