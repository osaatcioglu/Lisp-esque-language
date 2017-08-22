import sys

from repl import repl
from interpreter import interpreter

help_text = """More than one argument is given 
Usage:
lel [filename]
"""

if __name__ == "__main__":
	len_arguments = len(sys.argv) - 1
	is_success = True
	if len_arguments == 0:
		is_success = repl()
	elif len_arguments == 1:
		is_success = interpreter(sys.argv[1])
	else:
		print(help_text)
		is_success = False
	
	# exit to the system with the proper signal
	sys.exit(0 if is_success else 1)

