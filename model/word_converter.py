from pdf2docx import Converter

class PDFWord:
    def word_maker(self,file):
        try:
            file_object = Converter(file)
            file_name = file.split(".")[0]+"converted"+".docx"
            file_object.convert(file_name)
            return 0

        except Exception as e:
            print(e)
            return 1