
def read_file(file_name):
	read_data = None
	try:
		with open(file_name, "r+b") as f:
			read_data = f.read().decode("utf-8") 
	except:
		raise Exception("Couldn't read the file. Please check the filename and the path.")
	return read_data
