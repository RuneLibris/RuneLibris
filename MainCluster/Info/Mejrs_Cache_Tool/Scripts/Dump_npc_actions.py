from rs3 import *

import itertools

npc_configs = get_npc_configs()


#for id_local in itertools.product(range(100), range(200)): //do not work
#for id_local in itertools.product(range(100)): //do not work
#for id_local in itertools.product(100): //do not work
for id_local in itertools.count(start=0, step=1):
	name = npc_configs[id_local].name
	id = npc_configs[id_local].id
	actions = npc_configs[id_local].actions
	member_actions = npc_configs[id_local].member_actions
	if name is not None:
		print(f"RS/NPCs/{name} (ID {id})__{actions}__{member_actions}")