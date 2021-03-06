"""
@translate('function_name')
When used before a function, will tell rbx.py to translate when the function is used into the function name given

i.e.
@translate('math.sqrt')
def sqrt(*args, **kwargs):
    pass

@translate('function_name', 'include')
Same as translate with one parameter, but will include an rbx.py library as well.

When a script used this function, and is compiled, rbx.py will interpret it as "math.sqrt"
"""
class translate: #Note: Classes should usually be CamelCase, but because this is used as a decorator, it is lowercase
    def __init__(self, translation, include=None):
        pass

    def __call__(self, original_func):
        def wrapper(*args, **kwargs):
            pass

        return wrapper
