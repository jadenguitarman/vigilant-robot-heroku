from flask import Flask, request
from werkzeug.utils import secure_filename as secure
import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2, os, pickle

app = Flask(__name__)
MYDIR = os.path.dirname(__file__)

@app.route('/')
def home():
    return "<form method='post' action='/search' enctype='multipart/form-data'><input name='to_search' type='file'><input type='submit'></form>"
	
@app.route("/search", methods=["GET", "POST"])
def search():
	if request.method == "POST":
		print(request.files)
		if "to_search" not in request.files:
			return "Error, valid requests include a 'to_search' parameter."
		file = request.files["to_search"]
		print(file)
		if (file.filename == "") or ("." not in file.filename) or (file.filename.split('.')[-1].lower() not in ["png", "jpeg", "jpg"]):
			return "[]"
		file.filename = secure(file.filename)	
		img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
		return filename
	else:
		return "Hi there. This endpoint is restricted to POST requests, so please check the docs if you're trying to use the Vigilant Robot REST API. Thanks!"

@app.route("/train")
def train():
	np.random.seed(7)
	fashion_mnist = keras.datasets.fashion_mnist
	(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
	class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'] 
	train_images = train_images / 255.0
	test_images = test_images / 255.0
	model = keras.Sequential([
		keras.layers.Flatten(input_shape=(28, 28)),
		keras.layers.Dense(128, activation=tf.nn.relu),
		keras.layers.Dense(10, activation=tf.nn.softmax)
	])
	model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
	model.fit(train_images, train_labels, epochs=1)
	test_loss, test_acc = model.evaluate(test_images, test_labels)
	print('Test accuracy:', test_acc)
	model_json = model.to_json()
	model_weights = model.get_weights()
	to_return = model_json + "\n\n\n\n\n\n\n\n\n\n" + str(pickle.dumps(model_weights), 'latin1')
	return to_return

if __name__ == '__main__':
	app.run(use_reloader=True, debug=True)