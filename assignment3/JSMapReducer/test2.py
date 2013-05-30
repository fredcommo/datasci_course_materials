def Mapper(data):
	newData = {}
	for key in data.keys():
		newData = dict(newData.items() + dict([(k,key.count(k)) for k in list(key)]).items())
	counts_map = eval(newData)  	# makes a dict (associative array)
	for key in counts_map:
		count = counts_map[key]
		jsmr_context.Emit(key, str(count)) 

Mapper({ 'Apples':3, 'Bananas':5, 'Cherries':7 })
