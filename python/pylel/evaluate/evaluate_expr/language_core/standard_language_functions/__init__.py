from .lel_boolean import LEL_BOOLEAN
from .lel_general import LEL_GENERAL
from .lel_list import LEL_LIST
from .lel_math import LEL_MATH
from .lel_string import LEL_STRING
from .lel_bit import LEL_BIT

STANDARD = LEL_GENERAL.copy()
STANDARD.update(LEL_BOOLEAN)
STANDARD.update(LEL_MATH)
STANDARD.update(LEL_LIST)
STANDARD.update(LEL_STRING)
STANDARD.update(LEL_STRING)
STANDARD.update(LEL_BIT)
