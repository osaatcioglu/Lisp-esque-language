from __future__ import print_function
import sys
import functools
from pylel.token import Symbols, Token
from pylel.tools import is_int

EMPTY_LIST = Token(Symbols.LIST, [])

def _pretty_string(token):
	if token.type in [Symbols.NUMBER, Symbols.BOOLEAN, Symbols.STRING]:
		# Not all numbers are float. Fixing it before printing
		if token.type == Symbols.NUMBER:
			return str(int(token.value) if is_int(token.value) else token.value)
		return str(token.value)
	elif token.type == Symbols.LIST:
		return "(" + ", ".join((_pretty_string(item) for item in token.value)) + ")"
	return str(token)

def _exit(code_token):
	code = code_token.value if (code_token and code_token.type == Symbols.NUMBER) else 0
	sys.exit(code)

def _print(*items):
	out = "".join((_pretty_string(item) for item in items))
	print(out, end='')
	return Token(Symbols.STRING, out)

def _cls():
	print("\033c")
	return EMPTY_LIST

def _concat(*concatables):
	if not concatables:
		return EMPTY_LIST
	token = concatables[0].type
	all_same_type = all((concatable.type == token for concatable in concatables))

	if token == Symbols.LIST and all_same_type:
		return Token(Symbols.LIST, (item \
			for sublist in concatables for item in sublist.value))
	else:
		return functools.reduce(lambda acc, cur: \
			Token(Symbols.STRING, acc.value + cur.value \
			if cur.type in [Symbols.STRING, Symbols.NUMBER, Symbols.BOOLEAN] \
			else str(cur)), concatables)

LEL_GENERAL = {
	"exit": _exit,
	"print": _print,
	"cls": _cls,
	"concat": _concat,
}





