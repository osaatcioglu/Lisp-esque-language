
def read_file(file_name):
	read_data = None
	try:
		with open(file_name) as f:
			read_data = f.read()
		f.closed
	except:
		read_data = None
	return read_data
