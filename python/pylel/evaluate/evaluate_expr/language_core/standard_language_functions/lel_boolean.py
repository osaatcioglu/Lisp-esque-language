from pylel.token import Symbols, Token

LEL_BOOLEAN = {
	'=': lambda x, y: Token(Symbols.BOOLEAN, x.value == y.value ),
	'<': lambda x, y: Token(Symbols.BOOLEAN, x.value < y.value ),
	'>': lambda x, y: Token(Symbols.BOOLEAN, x.value > y.value ),
	'<=': lambda x, y: Token(Symbols.BOOLEAN, x.value <= y.value ),
	'>=': lambda x, y: Token(Symbols.BOOLEAN, x.value >= y.value ),
}
