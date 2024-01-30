from flask import render_template, request, send_file, Flask
import PDFCropper
import os

app = Flask(__name__)

@app.route("/")
def upload():
    return render_template("index.html")
@app.route("/crop")
def crop():
    return render_template("cropper_home.html")

@app.route("/merge")
def merge():
    return render_template("merger_home.html")

@app.route("/word")
def word():
    return render_template("word_home.html")

@app.route("/success",methods=["POST"])
def success():
    success.start_page=int(request.form['start'])
    success.end_page=int(request.form['end'])
    f=request.files['file']
    success.file_name=f.filename
    f.save(success.file_name)
    return render_template("success.html",start=success.start_page,
                           end=success.end_page,name=success.file_name)

@app.route("/convert")
def cropper():
    flag = PDFCropper.cropper(success.start_page,success.end_page,success.file_name)
    if(flag == 0):
        return render_template("download.html")
    elif(flag == 1):
        os.remove(success.file_name)
        msg = "Format Error: Please upload non encrypted PDF file."
        return render_template("exception.html",msg = msg)
    else:
        msg = f"""Failed: The PDF has only {flag} pages. Correct the range:"""
        os.remove(success.file_name)
        return render_template("exception.html", msg = msg)



@app.route("/download")
def download():
    try:
        try:
            filename=success.file_name.split(".")[0]+"cropped.pdf"
            return send_file(filename,as_attachment=True)
        finally:
            os.remove(filename)
            os.remove(success.file_name)
    except:
        msg = "File can be downloaded only once. Reload the application and try again."
        return render_template("exception.html",msg = msg)

@app.errorhandler(404)
def message(msg):
    msg = "Something went wrong. Please try again."
    return render_template("exception.html",msg=msg)



if __name__ == "__main__":
    app.run(debug=True)