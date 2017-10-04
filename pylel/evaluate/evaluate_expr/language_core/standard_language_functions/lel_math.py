import functools
from pylel.token import Symbols, Token

def _addition(*numbers):
	if any([number.type != Symbols.NUMBER for number in numbers]):
		raise Exception("+ only operates on NUMBER type")
	return functools.reduce(lambda acc, cur: Token(Symbols.NUMBER, acc.value + cur.value), numbers)

def _subtraction(x_number, y_number):
	if x_number.type != Symbols.NUMBER or y_number.type != Symbols.NUMBER:
		raise Exception("- only operates on NUMBER type")
	return Token(Symbols.NUMBER, x_number.value - y_number.value)

def _division(x_number, y_number):
	if x_number.type != Symbols.NUMBER or y_number.type != Symbols.NUMBER:
		raise Exception("/ only operates on NUMBER type")
	if y_number.value == 0:
		raise Exception("Divison by zero error")
	return Token(Symbols.NUMBER, x_number.value / y_number.value)

def _multiplication(*numbers):
	if any([number.type != Symbols.NUMBER for number in numbers]):
		raise Exception("* only operates on NUMBER type")
	return functools.reduce(lambda acc, cur: Token(Symbols.NUMBER, acc.value * cur.value), numbers)

def _power(x_number, y_number):
	if x_number.type != Symbols.NUMBER or y_number.type != Symbols.NUMBER:
		raise Exception("** only operates on NUMBER type")
	return Token(Symbols.NUMBER, pow(x_number.value, y_number.value))

def _mod(x_number, y_number):
	if x_number.type != Symbols.NUMBER or y_number.type != Symbols.NUMBER:
		raise Exception("% only operates on NUMBER type")
	if y_number.value == 0:
		raise Exception("Divison by zero error")
	return Token(Symbols.NUMBER, x_number.value % y_number.value)

LEL_MATH = {
	"+": _addition,
	"-": _subtraction,
	"*": _multiplication,
	"/": _division,
	"**": _power,
	"%": _mod,
}
