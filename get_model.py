import h5py, pickle, numpy

with open("train2.txt", "r") as f:
    b = f.read()

encoded = b.encode("latin1")
unpickled = pickle.loads(encoded)
#h5f = h5py.File('model.h5', 'w')
#h5f.create_dataset('dataset_1', data=a)
