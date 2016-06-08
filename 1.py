db = {1:('COMPUTER',1000.5,100),
 		      2:('MOUSE',10.0,300),
		      3:('PENCIL BLUE',0.50,500),
		      4:('PENCIL RED',0.50,600),
		      5:('PENCIL WHITE',0.50,900),
		      6:('HEADPHONES',15.7,500),
		      7:('Japanses Noodles',1.1,500),
}
row = (None,0.0,0)
try:
	row = db[id]
except:
		None
print row

operators = {'+': 'Add', '-': 'Subtract', '*': 'Multiply', '/': 'Divide'}

print operators.get('+')