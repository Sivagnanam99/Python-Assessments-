from jproperties import Properties

configs = Properties()
with open('samples.ini', 'rb') as read_prop:
	configs.load(read_prop)
	
prop_view = configs.items()
print(type(prop_view))

for item in prop_view:
	print(item)
