import sys

from repl import repl
from interpreter import interpreter

help_text = "More than one argument is given\nUsage:\nlel [filename]"

def main(argv):
	sys.setrecursionlimit(0x100000)
	len_arguments = len(argv)
	try:
		if len_arguments == 0:
			repl()
		elif len_arguments == 1:
			interpreter(argv[0])
		else:
			print(help_text)
	except Exception as e:
		print(str(e))
		sys.exit(1)

if __name__ == "__main__":
	main(sys.argv[1:])
