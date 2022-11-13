def deldubl(spisok):
	for x in spisok: 
		if spisok.count(x) > 1: 
			spisok.remove(x) 
	print(spisok) 

spisok = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]
deldubl(spisok)
