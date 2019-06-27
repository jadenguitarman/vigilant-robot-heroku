from flask import Flask, request
from werkzeug.utils import secure_filename as secure
import tensorflow, cv2
app = Flask(__name__)

@app.route('/')
def home():
    return "<form method='post' action='/search'><input name='to_search' type='file' enctype='multipart/form-data'><input type='submit'></form>"
	
@app.route("/search", methods=["POST"])
def search():
	file = request.files["to_search"]
	print(file)
	if (file.filename == "") or ("." not in file.filename) or (file.filename.split('.')[-1].lower() not in ["png", "jpeg", "jpg"]):
		return "[]"
	file.filename = secure(file.filename)	
	img = cv2.imdecode(numpy.fromstring(file.read(), numpy.uint8), cv2.IMREAD_UNCHANGED)
	return filename
	
if __name__ == '__main__':
	app.run(use_reloader=True)