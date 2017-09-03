from token import Symbols
from evaluate.scope import Scope
from evaluate.evaluate_expr.find_base_path import find_base_path
from token import tokenise
from tools import read_file, get_real_dir_name
from os import path

def lel_import(evaluate_expr, scope, expr):
	from interpreter import interpreter
	filename = evaluate_expr(scope, expr[1])
	if filename.type != Symbols.STRING:
		raise Exception("Import path must resolve to a string. Got {}"\
			.format(filename))
	file_path = path.join(find_base_path(scope), filename.value)
	base_path = get_real_dir_name(file_path)
	ast = interpreter(file_path)
	module_scope = Scope(None, base_path)
	return evaluate_expr(module_scope, ast)

