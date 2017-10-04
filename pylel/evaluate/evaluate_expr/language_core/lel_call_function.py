from pylel.evaluate.scope import Scope

def lel_call_function(evaluate_expr, scope, args, function_descriptor):
	# Every time the function runs it gets it's own scope, 
	# meaning variables set inside this function
	# will not persist across different calls.
	execution_scope = Scope(function_descriptor.scope)
	if len(args) != len(function_descriptor.expected_arguments):
		raise Exception("Expected {} arguments for function {} but got {}"\
			.format(len(function_descriptor.expected_arguments), \
				function_descriptor.name, len(args)))

	# Place arguments into the execution scope
	for i, argument in enumerate(args):
		execution_scope.variables[function_descriptor.expected_arguments[i]] = \
		argument
	body_evaluators = [evaluate_expr(execution_scope, f_expr)\
		for f_expr in function_descriptor.body_expressions]
	return body_evaluators[-1]
