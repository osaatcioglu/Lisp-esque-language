import os
from pylel.token import Symbols, Token
from pylel.tools import read_file

def _perform_read_file_sync(scope):
	def func(file_name, encoding):
		if file_name.type == Symbols.STRING and encoding.type == Symbols.STRING:
			from pylel.evaluate.evaluate_expr import find_base_path
			file_name = os.path.join(find_base_path(scope), file_name.value)
			return Token(Symbols.STRING, read_file(file_name, encoding.value))
		else:
			raise Exception("Requires filename and encoding to be strings. Got {} and {}"\
					.format(file_name, encoding))
	return func


def read_file_sync(evaluate_expr, scope, expr):
	if len(expr) < 3:
		raise Exception("Requires filename and encoding.")
	return _perform_read_file_sync(scope)\
	(evaluate_expr(scope, expr[1]), evaluate_expr(scope, expr[2]))
