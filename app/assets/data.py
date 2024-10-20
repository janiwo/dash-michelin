from typing import List


try:
    from data.objects.michelin_data.michelin import MichelinData
except ImportError:
    import sys

    sys.path.append(sys.path[0] + "/..")
    from data.objects.michelin_data.michelin import MichelinData


data = MichelinData()
all_restaurant_ids: List[int] = data.df[data.columns.code.restaurant_id].to_list()
