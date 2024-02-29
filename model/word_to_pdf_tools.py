from docx2pdf import convert

class WordtoPDF:
    def word_to_pdf_converter(self,file):
        try:
            outfile = file.split(".")[0]+"_converted.pdf"
            convert(file, outfile)
            return 0
        except:
            return 1