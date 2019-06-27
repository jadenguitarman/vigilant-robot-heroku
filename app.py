from flask import Flask, request
from werkzeug.utils import secure_filename as secure
import tensorflow, cv2
app = Flask(__name__)

@app.route('/')
def home():
    return "<form method='post' action='/search'><input name='to_search' type='file' enctype='multipart/form-data'><input type='submit'></form>"
	
@app.route("/search", methods=["GET", "POST"])
def search():
	if request.method == "POST":
		print(request.files)
		file = request.files["to_search"]
		print(file)
		if (file.filename == "") or ("." not in file.filename) or (file.filename.split('.')[-1].lower() not in ["png", "jpeg", "jpg"]):
			return "[]"
		file.filename = secure(file.filename)	
		img = cv2.imdecode(numpy.fromstring(file.read(), numpy.uint8), cv2.IMREAD_UNCHANGED)
		return filename
	else:
		return "Hi there. This endpoint is restricted to POST requests, so please check the docs if you're trying to use the Vigilant Robot REST API. Thanks!"
	
if __name__ == '__main__':
	app.run(use_reloader=True, debug=True)