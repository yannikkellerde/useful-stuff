import numpy as np
from itertools import groupby

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def analayze_list_structure(obj):
    if type(obj) not in (list,tuple):
        if isinstance(obj,np.ndarray):
            return f"Array_{obj.dtype}{obj.shape}"
        else:
            return type(obj).__name__
    else:
        out = []
        for el in obj:
            out.append(analayze_list_structure(el))
        if all_equal(out):
            return f"{type(obj).__name__}{{len={len(obj)}}}({out[0]})"
        else:
            if len(out) > 5:
                return f"{type(obj).__name__}{{len={len(out)}}}({out[0]})"
            else:
                return ", ".join(out)
