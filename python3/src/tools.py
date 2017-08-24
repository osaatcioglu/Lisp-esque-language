
def read_file(file_name):
	read_data = None
	try:
		with open(file_name, "r+b") as f:
			read_data = f.read().decode("utf-8") 
	except:
		read_data = None
	return read_data
