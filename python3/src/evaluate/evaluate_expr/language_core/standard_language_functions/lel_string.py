from token import Symbols, Token

def _split(string):
	if string.type != Symbols.STRING:
		raise Exception("Can't split non-strings. Got {}".format(string.type))
	return Token(Symbols.LIST, [Token(Symbols.STRING, c) for c in string])

lel_string = {
	"split": _split
}
