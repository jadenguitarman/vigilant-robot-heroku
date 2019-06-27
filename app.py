from flask import Flask, request
from werkzeug.utils import secure_filename as secure
import tensorflow, json
app = Flask(__name__)

@app.route('/')
def home():
    return "<form method='post' action='/search'><input name='to_search' type='file'><input type='submit'></form>"
	
@app.route("/search", methods=["POST"])
@cross_origin()
def search():
	print(request.files)
	if ("to_search" not in request.files):
		return "a"
	if (request.files["to_search"].filename == ""):
		return "b";
	if ("." not in request.files["to_search"].filename):
		return "c"; 
	if (request.files["to_search"].filename.split('.')[-1].lower() not in ["png", "jpeg", "jpg"]):
		return "[]"
	file = request.files[0]
	filename = secure(file.filename)
	return filename
	
if __name__ == '__main__':
	app.run(use_reloader=True)