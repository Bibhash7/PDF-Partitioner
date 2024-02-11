from PyPDF2 import PdfWriter,PdfReader

class Cropper:
    def cropper(self, startpage, endpage, file):
        if(startpage !=  0):
            startpage -=1

        try:
            file_object = open(file,"rb")
            input_pdf = PdfReader(file_object)
            if(startpage > len(input_pdf.pages) or endpage > len(input_pdf.pages) or startpage > endpage):
                return len(input_pdf.pages)

            out_pdf = PdfWriter()
            with open(file.split(".")[0]+"cropped"+".pdf","wb") as ostream:
                for page in range(startpage, endpage):
                  out_pdf.add_page(input_pdf.pages[page])
                  out_pdf.write(ostream)
            return 0

        except:
            return 1

        finally:
            file_object.close()
