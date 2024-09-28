from dataclasses import dataclass, field
import pickle
from decouple import config
import os
from typing import Optional

import pandas as pd


@dataclass(frozen=True)
class MichelinNormalizedColumns:
    name: str = "name"
    address: str = "address"
    location: str = "location"
    price: str = "price"
    cuisine: str = "cuisine"
    longitude: str = "longitude"
    latitude: str = "latitude"
    phone_number: str = "phone_number"
    michelin_url: str = "michelin_url"
    website_url: str = "website_url"
    award: str = "award"
    has_green_star: str = "green_star"
    facilities_and_services: str = "facilities_and_services"
    description: str = "description"


@dataclass(frozen=True)
class MichelinCodeColumns:
    location_city: str = "location_city"
    location_country: str = "location_country"
    price_currency: str = "price_currency"
    price_amount: str = "price_amount"
    award_stars_count: str = "award_stars_count"
    award_has_stars: str = "award_has_stars"


@dataclass(frozen=True)
class MichelinExtrasColumns:
    has_air_conditioning: str = "Air conditioning"
    is_booking_essential: str = "Booking essential"
    is_dinner_booking_essential: str = "Booking essential - dinner"
    is_bring_your_own_bottle: str = "Bring your own bottle"
    has_brunch: str = "Brunch"
    has_car_park: str = "Car park"
    is_cash_only: str = "Cash only"
    is_cash_only_lunch: str = "Cash only - lunch"
    has_counter_dining: str = "Counter dining"
    has_no_credit_card: str = "Credit cards not accepted"
    has_no_foreign_credit_card: str = "Foreign credit cards not accepted"
    has_garden_or_park: str = "Garden or park"
    has_great_view: str = "Great view"
    has_interesting_wine_list: str = "Interesting wine list"
    has_notable_sake_list: str = "Notable sake list"
    has_vegetarian_menus: str = "Restaurant offering vegetarian menus"
    has_shoes_removed: str = "Shoes must be removed"
    has_terrace: str = "Terrace"
    has_valet_parking: str = "Valet parking"
    has_wheelchair_access: str = "Wheelchair access"


@dataclass(frozen=True)
class MichelinColumns:
    norm: MichelinNormalizedColumns = MichelinNormalizedColumns()
    code: MichelinCodeColumns = MichelinCodeColumns()
    extras: MichelinExtrasColumns = MichelinExtrasColumns()


@dataclass
class MichelinData:
    df: Optional[pd.DataFrame] = field(default=None)
    columns: MichelinColumns = MichelinColumns()
    path: Optional[str] = os.path.join(config("DATA_VAULT_PATH"), "michelin.pkl")

    def __post_init__(self):

        if self.df is None:

            self.df = self.load_data(self.path)

    def load_data(self, path: str) -> pd.DataFrame:

        with open(path, "rb") as f:
            df = pickle.load(f)

        return df

    def save_data(self, path: Optional[str] = None) -> None:

        if path is None:
            path = self.path

        with open(path, "wb") as f:
            pickle.dump(self.df, f)
