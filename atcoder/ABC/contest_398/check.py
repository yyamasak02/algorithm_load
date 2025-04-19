route_index = (0, 0)
smocks = set()
smocks.add(route_index)
route_index[0] -= 2
smocks.add(route_index)

for smock in smocks:
	print(smock)