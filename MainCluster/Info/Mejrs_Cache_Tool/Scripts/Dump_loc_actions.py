from rs3 import *

import itertools

loc_configs = get_location_configs()


#for id_local in itertools.product(range(100), range(200)): //do not work
#for id_local in itertools.product(range(100)): //do not work
#for id_local in itertools.product(100): //do not work
for id_local in itertools.count(start=0, step=1):
	name = loc_configs[id_local].name
	id = loc_configs[id_local].id
	actions = loc_configs[id_local].actions
	member_actions = loc_configs[id_local].member_actions
	if name is not None:
		print(f"RS/Locs/{name} (ID {id})__{actions}__{member_actions}")