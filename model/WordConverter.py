from pdf2docx import Converter

class PDFWord:
    def wordMaker(file):
        try:
            fileobject = Converter(file)
            filename = file.split(".")[0]+"converted"+".docx"
            fileobject.convert(filename)
            return 0
        except Exception as e:
            print(e)
            return 1