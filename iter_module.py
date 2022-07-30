import importlib
import pkgutil

def iter_module(module_name,shorten=False):
    try:
        module = importlib.import_module(module_name)
    except Exception as e:
        print(e)
        return {}
    result = {module_name:module}
    if not hasattr(module,"__path__"):
        return result
    subnames = [str(x.name) for x in pkgutil.iter_modules(module.__path__)]
    for subname in subnames:
        subres = iter_module(module_name+"."+subname)
        if shorten:
            subres = {key.split(".")[-1]:value for key,value in subres.items()}
        result.update(subres)
    return result
