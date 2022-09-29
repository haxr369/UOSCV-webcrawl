import os, sys
from flask import Flask, escape, request,  Response, g, make_response, redirect, url_for,flash
from flask.templating import render_template
from werkzeug.utils import secure_filename
#from werkzeug import secure_filename
#from . import neural_style_transfer
 
UPLOAD_FOLDER = '/home/dir_v/crawl_site/UOSCV-webcrawl/helloflask/static/images'        

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/image_get',methods=['GET','POST'])
def image_get():
    if request.method =='POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        f = request.files['file']

        if f.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('nst_post',filename=filename))
    else:
        return render_template('image_get.html')

@app.route('/show_classification', methods=['GET','POST'])
def nst_post():
    filename = request.args.get('filename')
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    

    return render_template('show_classification.html',img_path ='/images/'+filename)

if __name__ == '__main__':
    app.run()