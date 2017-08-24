from token import tokenise, Symbols
from tools import read_file
from parse import Parse

def validate(tokens):
	left = 0
	right = 0
	for token in tokens:
		if token.type == Symbols.LPAREN: left += 1 
		if token.type == Symbols.RPAREN: right += 1 
		if right > left:
			return False
	return left == right

def interpreter(file_name):
	data = read_file(file_name)
	if not data:
		print("Couldn't read the file. Please check the filename and the path.")
		return False
	tokens = tokenise(data)
	if not validate(tokens):
		print('Unmatched parentheses.')
		return False
	ast = Parse.parse(tokens)
	print(ast)
	return True
