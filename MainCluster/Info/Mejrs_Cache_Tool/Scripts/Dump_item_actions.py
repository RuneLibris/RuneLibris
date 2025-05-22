from rs3 import *

import itertools

item_configs = get_item_configs()


#for id_local in itertools.product(range(100), range(200)): //do not work
#for id_local in itertools.product(range(100)): //do not work
#for id_local in itertools.product(100): //do not work
for id_local in itertools.count(start=0, step=1):
	name = item_configs[id_local].name
	id = item_configs[id_local].id
	widget_actions = item_configs[id_local].widget_actions
	ground_actions = item_configs[id_local].ground_actions
	if name is not None:
		print(f"RS/Items/{name} (ID {id})__{widget_actions}__(members actions placeholder)__{ground_actions}")