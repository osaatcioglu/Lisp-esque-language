from token import Symbols, Token
from .lel_call_function import lel_call_function

def _perform_filtering(evaluate_expr, scope, expr, l):
	def func(filtering_function):
		if filtering_function.type != Symbols.FUNCTION_REFERENCE:
			raise Exception("Invalid function passed to filter. Got {}"\
				.format(expr))

		map_calls = list(map(\
			lambda v: lel_call_function(evaluate_expr, scope, \
				[v[0], Token(Symbols.NUMBER, v[1])], \
				filtering_function.value), enumerate(l.value)))

		new_list = list(filter(\
			lambda v: map_calls[v[1]].value, enumerate(l.value)))

		return Token(Symbols.LIST, new_list)
	return func

def _get_filtering_function(evaluate_expr, scope, expr):
	def func(l):
		if l.type != Symbols.LIST:
			raise Exception("Invalid list passed to filter. Got {}"\
				.format(expr))
		evaluted_expr = evaluate_expr(scope, expr[2])
		return _perform_filtering(evaluate_expr, scope, \
			expr, l)(evaluted_expr)
	return func

def lel_filter(evaluate_expr, scope, expr):
	return _get_filtering_function(evaluate_expr, scope, expr)\
	(evaluate_expr(scope, expr[1]))
