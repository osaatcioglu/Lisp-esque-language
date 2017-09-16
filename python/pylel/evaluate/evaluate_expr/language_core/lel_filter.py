from pylel.token import Symbols, Token
from .lel_call_function import lel_call_function

def _perform_filtering(evaluate_expr, scope, expr, lel_list):
	def func(filtering_function):
		if filtering_function.type != Symbols.FUNCTION_REFERENCE:
			raise Exception("Invalid function passed to filter. Got {}"\
				.format(expr))

		new_list = [token for i, token in enumerate(lel_list.value)\
			if lel_call_function(evaluate_expr, scope,\
				[token, Token(Symbols.NUMBER, i)], filtering_function.value).value]

		return Token(Symbols.LIST, new_list)
	return func

def _get_filtering_function(evaluate_expr, scope, expr):
	def func(lel_list):
		if lel_list.type != Symbols.LIST:
			raise Exception("Invalid list passed to filter. Got {}"\
				.format(expr))
		evaluted_expr = evaluate_expr(scope, expr[2])
		return _perform_filtering(evaluate_expr, scope, \
			expr, lel_list)(evaluted_expr)
	return func

def lel_filter(evaluate_expr, scope, expr):
	return _get_filtering_function(evaluate_expr, scope, expr)\
	(evaluate_expr(scope, expr[1]))
