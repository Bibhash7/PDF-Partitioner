from pdf2docx import Converter

def wordMaker(file):
    try:
        cv = Converter(file)
        filename = file.split(".")[0]+"converted"+".docx"
        cv.convert(filename)
    except Exception as e:
        print(e)

