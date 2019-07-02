
from functools import reduce

def pipe(arg, *fns):

    def through(a, b):
        return lambda x: b(a(x))

    pipe_line = reduce(through, fns, lambda x: x)
    return pipe_line(arg)
