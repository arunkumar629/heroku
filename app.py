import os
from flask import Flask, render_template, request
#from werkzeug import secure_filename
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploadfile():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join('static/', secure_filename(f.filename)))
      return render_template('result.html',result="/static/"+f.filename)
		
if __name__ == '__main__':
   app.run(debug = True)