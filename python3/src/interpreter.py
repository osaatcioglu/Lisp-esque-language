from token import tokenise
from tools import read_file

def interpreter(file_name):
	data = read_file(file_name)
	if not data:
		print("Couldn't read the file. Please check the filename and the path.")
		return False
	print(tokenise(data))
	return True
