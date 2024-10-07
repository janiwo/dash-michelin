try:
    from data.objects.michelin_data.michelin import MichelinData
except ImportError:
    import sys

    sys.path.append(sys.path[0] + "/..")
    from data.objects.michelin_data.michelin import MichelinData


data = MichelinData()
