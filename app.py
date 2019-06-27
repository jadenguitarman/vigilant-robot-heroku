from flask import Flask, request
from werkzeug.utils import secure_filename as secure
import tensorflow, json
app = Flask(__name__)

@app.route('/')
def home():
    return "<form method='post' action='/search'><input name='to_search' type='file'><input type='submit'></form>"
	
@app.route("/search", methods=["POST"])
def search():
	file = request.files.to_dict(flat=True)["to_search"]
	print(file)
	if (file.filename == ""):
		return "a";
	if ("." not in file.filename):
		return "b"; 
	if (file.filename.split('.')[-1].lower() not in ["png", "jpeg", "jpg"]):
		return "c"
	
	filename = secure(file.filename)
	return filename
	
if __name__ == '__main__':
	app.run(use_reloader=True)