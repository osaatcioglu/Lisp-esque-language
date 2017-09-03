
class Scope(object):
	def __init__(self, upper_scope, base_path = None):
		self.upper_scope = upper_scope
		self.variables = {}
		self.base_path = base_path

