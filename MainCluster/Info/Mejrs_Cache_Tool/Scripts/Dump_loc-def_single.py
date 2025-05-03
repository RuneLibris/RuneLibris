from rs3 import *

import itertools

loc_configs = get_location_configs()

name = loc_configs[45476].name
id = loc_configs[45476].id
print(f"{id} -- {name}")