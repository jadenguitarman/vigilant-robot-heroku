from flask import Flask, request
from werkzeug.utils import secure_filename as secure
import tensorflow
app = Flask(__name__)

@app.route('/')
def home():
    return "<form method='post' action='/search'><input type='file'><input type='submit'></form>"
	
@app.route("/search", methods=["POST"])
def search():
	if len(request.files) == 0 or request.files[0].filename == "" or "." not in request.files[0].filename or request.files[0].filename.rsplit('.', 1)[1].lower() not in ["png", "jpeg", "jpg"]:
		return "[]"
	file = request.files[0]
	filename = secure(file.filename)
	return filename
	
if __name__ == '__main__':
	app.run(use_reloader=True)