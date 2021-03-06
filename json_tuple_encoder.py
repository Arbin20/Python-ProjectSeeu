import json

class MultiDimensionalArrayEncoder(json.JSONEncoder):
    def encode(self, obj):
        def hint_tuples(item):
            if isinstance(item, tuple):
                return {'__tuple__': True, 'items': item}
            if isinstance(item, list):
                return [hint_tuples(e) for e in item]
            else:
                return item

        return super(MultiDimensionalArrayEncoder, self).encode(hint_tuples(obj))

def hinted_tuple_hook(obj):
    if '__tuple__' in obj:
        return tuple(obj['items'])
    else:
        return obj

data = [("15/6/2021",48),("15/6/2021",50),("15/6/2021",54),("15/6/2021",56),("15/6/2021",34)]

enc = MultiDimensionalArrayEncoder()

jsonstring =  enc.encode(data)

print(jsonstring)

# [1, 2, {"items": [3, 4], "__tuple__": true}, [5, 6, {"items": [7, 8], "__tuple__": true}]]
print("\n\n")
print(json.loads(jsonstring, object_hook=hinted_tuple_hook))

# [1, 2, (3, 4), [5, 6, (7, 8)]]

# if __name__ == '__main__':
#     main()