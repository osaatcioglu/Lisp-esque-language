import os
from require import require
from pylel.tools import get_real_dir_name
from pylel.libraries import LIBRARIES

LIBRARY_LOCATION = "../../../libraries/"
LIBRARY_EXTENSION = ".py"
LIBRARY_SEPARATOR = "-"

def lel_use(evaluate_expr, scope, expr):
	if len(expr) != 2:
		raise Exception("Use requires only 1 argument. Got {} at expression {}"\
			.format(len(expr), expr))
	library = os.path.join(get_real_dir_name(__file__),\
	LIBRARY_LOCATION, expr[1].value + LIBRARY_EXTENSION)
	library_methods = require(str(library)).METHODS
	LIBRARIES.update({
		expr[1].value + LIBRARY_SEPARATOR + k: library_methods[k] \
		for k in library_methods.keys()
	})
