import json

json_string = '{"key":"value"}'
print(json.loads(json_string))


a = json.loads(json_string)


import pickle
pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))
