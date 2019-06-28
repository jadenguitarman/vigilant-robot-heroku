import h5py, pickle, numpy, io

with io.open("train.txt", "r", encoding="latin1") as f:
    b = f.read()

encoded = b.encode("latin1")
unpickled = pickle.loads(encoded)
#h5f = h5py.File('model.h5', 'w')
#h5f.create_dataset('dataset_1', data=a)
