from assets.data import data


stars_hierarchy = [
    "Selected Restaurants",
    "Bib Gourmand",
    "1 Star",
    "2 Stars",
    "3 Stars",
]

countries_list = sorted(data.df[data.columns.code.location_country].dropna().unique())
facilities_and_services = sorted(
    data.df[data.columns.norm.facilities_and_services].explode().dropna().unique()
)
