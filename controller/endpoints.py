from app import app
from flask import render_template, request, send_file
from model.cropper_tools import Cropper
from model.word_converter import PDFWord
from model.merger_tools import Marger
from model.word_to_pdf_tools import WordtoPDF
import os

list_of_files = []

cropper_object = Cropper()
word_converter_object = PDFWord()
merger_object = Marger()
docx_to_pdf_object = WordtoPDF()

@app.route("/")
def upload():
    return render_template("index.html")

@app.route("/crop")
def crop_pdf():
    return render_template("cropper_home.html")

@app.route("/merge")
def merge_pdf():
    return render_template("merger_home.html")

@app.route("/word")
def to_word():
    return render_template("word_home.html")

@app.route("/docxtopdf")
def docx_to_pdf():
    return render_template("word_to_pdf_home.html")

@app.route("/success/<page_id>",methods = ["POST"])
def success(page_id):
    route = int(page_id)
    if route == 1:
        success.start_page = int(request.form['start'])
        success.end_page = int(request.form['end'])
        file_object = request.files['file']
        success.file_name = file_object.filename
        file_object.save(success.file_name)
        return render_template("success.html", start = success.start_page,
                               end = success.end_page, name = success.file_name)

    elif route == 2:
        file_object = request.files['file']
        success.file_name = file_object.filename
        file_object.save(success.file_name)
        return render_template("success_word.html", name = success.file_name)

    elif route == 3:
        file_list_object = request.files.getlist("files")
        for file_object in file_list_object:
            file_object.save(file_object.filename)
            list_of_files.append(file_object.filename)
        return render_template("success_merge.html")

    elif route == 4:
        file_object = request.files['file']
        success.file_name = file_object.filename
        file_object.save(success.file_name)
        return render_template("success_word_to_pdf.html", name=success.file_name)


@app.route("/convert/<page_id>")
def convert(page_id):
    route = int(page_id)
    if route == 1:
        flag = cropper_object.cropper(success.start_page, success.end_page, success.file_name)
        if(flag == 0):
            return render_template("download.html")

        elif(flag == 1):
            os.remove(success.file_name)
            error_format_mismatch_message = "Format Error: Please upload non encrypted PDF file."
            return render_template("exception.html", message = error_format_mismatch_message)

        else:
            error_range_message = f"""Failed: The PDF has only {flag} pages. Correct the range:"""
            os.remove(success.file_name)
            return render_template("exception.html", message = error_range_message)

    elif route == 2:
        flag = word_converter_object.word_maker(success.file_name)
        if flag == 0:
            return render_template("download_word.html")

        else:
            error_file_upload_message = "Some Error occured while uploading file."
            return render_template("exception.html", message = error_file_upload_message)

    elif route == 3:
        flag = merger_object.merge_pdf(list_of_files)
        if flag == 0:
            print(flag)
            return render_template("download_merge.html")
        else:
            error_merge_message = "Failed: Some exception occured while merging"
            return render_template("exception.html",message = error_merge_message)

    elif route == 4:
        flag = docx_to_pdf_object.word_to_pdf_converter(success.file_name)
        if flag == 0:
            print(flag)
            return render_template("download_pdf.html")
        else:
            error_word_to_pdf_message = "Failed: Some exception occured."
            return render_template("exception.html", message=error_word_to_pdf_message)



@app.route("/download/<page_id>")
def download(page_id):
    route = int(page_id)
    if route == 1:
        try:
            try:
                file_name = success.file_name.split(".")[0]+"cropped.pdf"
                return send_file(file_name, as_attachment = True)

            finally:
                os.remove(file_name)
                os.remove(success.file_name)

        except:
            error_download_message = "File can be downloaded only once. Reload the application and try again."
            return render_template("exception.html",message = error_download_message)

    elif route == 2:
        try:
            filename = success.file_name.split(".")[0]+"converted.docx"
            return send_file(filename, as_attachment = True)

        except:
            error_word_message = "Some Exception occured."
            return render_template("exception.html", message = error_word_message)

    elif route == 3:
        try:
            filename = "merged.pdf"
            return send_file(filename, as_attachment= True)
        except:
            error_merge_message = "Some Exception occured."
            return render_template("exception.html", message=error_merge_message)

    elif route == 4:
        try:
            filename = success.file_name.split(".")[0] + "_converted.pdf"
            return send_file(filename, as_attachment=True)
        except:
            error_word_to_pdf_message = "Some Exception occured."
            return render_template("exception.html", message=error_word_to_pdf_message)


@app.errorhandler(404)
def page_not_found(message):
    error_404_message = "Something went wrong. Please try again."
    return render_template("exception.html", message = error_404_message)