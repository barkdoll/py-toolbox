

# Stolen from:
# https://stackoverflow.com/a/2158532

def flatten(l):

    for item in l:

        if (isinstance(item, collections.Iterable) and not
                isinstance(item, (str, bytes))):
            yield from flatten(item)

        else:
            yield el
