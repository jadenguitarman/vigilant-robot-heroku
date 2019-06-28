from flask import Flask, request
from werkzeug.utils import secure_filename as secure
import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2, json

app = Flask(__name__)

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
		if (file.filename == "") or ("." not in file.filename) or (file.filename.split('.')[-1].lower() not in ["png", "jpeg", "jpg"]):
			return "[]"
		file.filename = secure(file.filename)
		with open("model.json") as f:
			model = keras.models.model_from_json(f.read())
		with open("model.txt") as f:
			model.set_weights([np.fromstring(k[2].encode("latin-1"), dtype=k[0]).reshape(tuple(k[1])) for k in json.loads(f.read())])
		img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
		img = cv2.resize(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), (28,28), interpolation=cv2.INTER_AREA) / 255
		print(img.shape)
		img = np.expand_dims(img,0)
		print(img.shape)
		class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'] 
		prediction = model.predict(img)[0]
		prediction.dtype = float
		prediction = json.dumps(dict(zip([class_names[x] for x in prediction], prediction)))
		
		return prediction
	else:
		return "Hi there. This endpoint is restricted to POST requests, so please check the docs if you're trying to use the Vigilant Robot REST API. Thanks!"

@app.route("/train")
def train():
	np.random.seed(7)
	fashion_mnist = keras.datasets.fashion_mnist
	(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
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
	model_weights = json.dumps([[str(k.dtype), list(k.shape), k.tostring().decode("latin-1")] for k in model_weights])
	to_return = model_json + "\n\n\n\n\n\n\n\n" + model_weights
	return to_return

if __name__ == '__main__':
	app.run(use_reloader=True, debug=True)