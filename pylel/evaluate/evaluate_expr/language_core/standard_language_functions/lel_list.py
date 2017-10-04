from pylel.token import Symbols, Token

EMPTY_LIST = Token(Symbols.LIST, [])

def _join(lel_list):
	if lel_list.type != Symbols.LIST:
		raise Exception("Can't join non-lists. Got {}".format(lel_list.type))
	return Token(Symbols.STRING, "".join([item.value for item in lel_list.value]))

def _length(lel_list):
	if lel_list.type != Symbols.LIST:
		raise Exception("length operates on LIST type. Got {}".format(lel_list.type))
	return Token(Symbols.NUMBER, len(lel_list.value))

def _head(lel_list):
	if lel_list.type != Symbols.LIST:
		raise Exception("head operates on LIST type. Got {}".format(lel_list.type))
	return lel_list.value[0] if lel_list.value else EMPTY_LIST

def _tail(lel_list):
	if lel_list.type != Symbols.LIST:
		raise Exception("tail operates on LIST type. Got {}".format(lel_list.type))
	return Token(Symbols.LIST, lel_list.value[1:])

def _nth(lel_list, nth_number):
	if lel_list.type != Symbols.LIST:
		raise Exception("nth operates on LIST type. Got {}".format(lel_list.type))
	nth = int(nth_number.value)
	if nth >= 0 and nth < len(lel_list.value):
		return lel_list.value[nth]
	raise Exception("nth: bad index {}. Given list has {} elements"\
		.format(nth_number.value, len(lel_list.value)))

def _sublist(lel_list, start, end):
	if lel_list.type != Symbols.LIST:
		raise Exception("sublist operates on LIST type. Got {}".format(lel_list.type))
	list_length = len(lel_list.value)
	start = int(start.value)
	end = int(end.value)

	if start > end:
		raise Exception("start index cannot be greater than the end index for a sublist")
	if start < 0 or end >= list_length:
		raise Exception("sublist indexes out of range. Got start ({}) end ({}) for list of length {}"\
			.format(start, end, list_length))
	return Token(Symbols.LIST, lel_list.value[start:end + 1])

LEL_LIST = {
	"join": _join,
	"length": _length,
	"head": _head,
	"tail": _tail,
	"nth": _nth,
	"sublist": _sublist
}
