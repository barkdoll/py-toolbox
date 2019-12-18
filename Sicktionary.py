
'''
I thought it would be better to not support object attribute notation 
because it seemed like it could cause some unexpected behaviors according to this SO answer.

https://stackoverflow.com/a/14620633
'''
class Sicktionary(dict):

    def __init__(self, dictionary):
        self.update(dictionary)

    def update(self, dictionary):
        for k, v in dictionary.items():
            self[k] = v


    def __getitem__(self, key):
        if key in self: 
            return self.get(key)

        return self.setdefault(key, Sicktionary({}))


    def __setitem__(self, key, value):
        real_value = Sicktionary(value) if isinstance(value, dict) else value
        dict.__setitem__(self, key, real_value)


    def is_empty(self):
        return not bool(self)

    def scrub(self, *value_filter):
        clean = Sicktionary({})

        for k, v in self.items():
            
            if isinstance(v, Sicktionary):
                nested = Sicktionary(v).scrub(*value_filter)
                if len(nested.keys()) > 0:
                    clean[k] = nested
            
            else:
                if v not in value_filter:
                    clean[k] = v
        
        return clean


    def filter(self, *disposables):
        clean = Sicktionary({})

        for k, v in self.items():
            
            if isinstance(v, Sicktionary):
                nested = Sicktionary(v).filter(*disposables)
                clean[k] = nested
            
            else:
                if v not in disposables:
                    clean[k] = v
        
        return clean
