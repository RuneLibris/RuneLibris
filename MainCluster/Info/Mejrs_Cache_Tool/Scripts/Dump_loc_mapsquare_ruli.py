from rs3 import *

import itertools

loc_configs = get_location_configs()


mapsquares = MapSquares()
"""
for i, j in itertools.product(range(100), range(200)):
	try:
		#sq = mapsquares.get(i, j)
		sq = mapsquares.get(57, 67)
		locations = sq.locations()
	except ValueError:
		# not a valid mapsquare
		pass
	except KeyError:
		# not a valid mapsquare
		pass
	except RuntimeError:
		# not a valid mapsquare
		pass
	except OSError: # will probably raise a different exception in the future
		# no locations
		pass
	except ArchiveNotFoundError:
		# manpaint edit
		pass
	except FileMissingError:
		# manpaint edit
		pass
	else:
"""
sq = mapsquares.get(57, 67)
locations = sq.locations()
for loc in locations:
	name = loc_configs[loc.id].name
	actions = loc_configs[loc.id].actions
	member_actions = loc_configs[loc.id].member_actions
	if name is not None:
		position = loc.plane,"|", loc.i << 6 | loc.x,"|", loc.j << 6 | loc.y
		#orig: print("|",position,"|",loc.i,"|",loc.j,"|",loc.id,"|",name,"|",actions,"|")
		#print("*",loc.i,loc.j + ";" + actions + ";" + member_actions + "[[RS/Locs/" + "(ID: " + loc.id + ")]]")
		#print(f"*{loc.i},{loc.j};{actions};{member_actions};[[RS/Locs/{name} (ID: {loc.id})|{name} (ID: {loc.id})]]")
		print(f"{{{{Maploc|{loc.i},{loc.j}|{actions};{member_actions}|[[RS/Locs/{name} (ID: {loc.id})|{name} (ID {loc.id})]]}}}}")
		#print("*[[RS/Locs/",name," (ID:",loc.id,")]] (",loc.i,",",loc.j,"," || ",actions,"||",member_actions,")")