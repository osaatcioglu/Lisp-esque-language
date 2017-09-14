import os

def read_file(file_name, encoding="utf-8"):
	read_data = None
	try:
		with open(file_name, "r+b") as f:
			read_data = f.read().decode(encoding)
	except:
		raise Exception("Couldn't read the file. Please check the filename and the path.")
	return read_data

def get_real_dir_name(file_name):
	return os.path.dirname(os.path.realpath(file_name))

def is_int(number):
	return number % 1 == 0
