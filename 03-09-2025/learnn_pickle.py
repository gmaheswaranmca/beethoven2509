import pickle
data = [{'a': 1, 'b': 2}, {'a': 2, 'b': 3}]
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)
    print('data saved.')
with open('data.pkl', 'rb') as f:
    loaded = pickle.load(f)
    print(loaded)