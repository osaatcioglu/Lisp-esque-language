from pylel.token import Symbols, Token

def _and(x_number, y_number):
	if x_number.type != Symbols.NUMBER or y_number.type != Symbols.NUMBER:
		raise Exception("- only operates on NUMBER type")
	return Token(Symbols.NUMBER, int(x_number.value) & int(y_number.value))

def _or(x_number, y_number):
	print("or")
	if x_number.type != Symbols.NUMBER or y_number.type != Symbols.NUMBER:
		raise Exception("- only operates on NUMBER type")
	return Token(Symbols.NUMBER, int(x_number.value) | int(y_number.value))

def _xor(x_number, y_number):
	if x_number.type != Symbols.NUMBER or y_number.type != Symbols.NUMBER:
		raise Exception("- only operates on NUMBER type")
	return Token(Symbols.NUMBER, int(x_number.value) ^ int(y_number.value))

def _not(x_number):
	if x_number.type != Symbols.NUMBER:
		raise Exception("- only operates on NUMBER type")
	return Token(Symbols.NUMBER, ~int(x_number.value))

def _left_shift(x_number, y_number):
	if x_number.type != Symbols.NUMBER or y_number.type != Symbols.NUMBER:
		raise Exception("- only operates on NUMBER type")
	return Token(Symbols.NUMBER, int(x_number.value) << int(y_number.value))

def _right_shift(x_number, y_number):
	if x_number.type != Symbols.NUMBER or y_number.type != Symbols.NUMBER:
		raise Exception("- only operates on NUMBER type")
	return Token(Symbols.NUMBER, int(x_number.value) >> int(y_number.value))

LEL_BIT = {
	"&": _and,
	"|": _or,
	"^": _xor,
	"~": _not,
	"<<": _left_shift,
	">>": _right_shift,
}
