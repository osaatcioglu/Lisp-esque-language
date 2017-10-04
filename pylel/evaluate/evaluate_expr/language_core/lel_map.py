from pylel.token import Symbols, Token
from .lel_call_function import lel_call_function

def _get_mapping_function(evaluate_expr, scope, expr):
	def func(lel_list):
		if lel_list.type != Symbols.LIST:
			raise Exception("Invalid list passed to map. Got {}"\
				.format(expr))
		return _perform_mapping(evaluate_expr, scope, expr, lel_list)(evaluate_expr(scope, expr[2]))
	return func

def _perform_mapping(evaluate_expr, scope, expr, lel_list):
	def func(mapping_function):
		if mapping_function.type != Symbols.FUNCTION_REFERENCE:
			raise Exception("Invalid function passed to map. Got {}"\
				.format(expr))
		map_calls = [lel_call_function(evaluate_expr, scope, [v[1], \
				Token(Symbols.NUMBER, v[0])], mapping_function.value)\
				for v in enumerate(lel_list.value)]
		return Token(Symbols.LIST, map_calls)
	return func

def lel_map(evaluate_expr, scope, expr):
	return _get_mapping_function(evaluate_expr, scope, expr)\
	(evaluate_expr(scope, expr[1]))
