from __future__ import absolute_import
import math as pymath
from pylel.token import Symbols, Token

def _sin(x_degree):
	if x_degree.type != Symbols.NUMBER:
		raise Exception("sin only operates on NUMBER type")
	return Token(Symbols.NUMBER, pymath.sin(x_degree.value))

def _cos(x_degree):
	if x_degree.type != Symbols.NUMBER:
		raise Exception("sin only operates on NUMBER type")
	return Token(Symbols.NUMBER, pymath.cos(x_degree.value))

METHODS = {
	"sin": _sin,
	"cos": _cos,
}
