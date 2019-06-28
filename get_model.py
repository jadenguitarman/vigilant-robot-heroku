import h5py, numpy, json

with open("train.txt") as f:
    inp = f.read()

model_weights = [numpy.fromstring(k[2].encode("latin-1"), dtype=k[0]).reshape(tuple(k[1])) for k in json.loads(inp)]
#h5f = h5py.File('model.h5', 'w')
#h5f.create_dataset('dataset_1', data=a)
