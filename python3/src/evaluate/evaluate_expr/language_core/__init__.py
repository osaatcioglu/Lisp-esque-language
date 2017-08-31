
from .lel_if import lel_if
from .lel_let import lel_let
from .lel_list import lel_list
from .lel_mutate import lel_mutate

core = {
	"if": lel_if,
	"let": lel_let,
    "list": lel_list,
    "mutate": lel_mutate,
}

