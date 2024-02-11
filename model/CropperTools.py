from PyPDF2 import PdfWriter,PdfReader

class Cropper:
    def cropper(startpage, endpage, file):
        if(startpage !=  0):
            startpage -=1
        try:
            fileObject = open(file,"rb")
            inputPdf = PdfReader(fileObject)
            if(startpage > len(inputPdf.pages) or endpage > len(inputPdf.pages) or startpage > endpage):
                return len(inputPdf.pages)
            outPdf = PdfWriter()
            with open(file.split(".")[0]+"cropped"+".pdf","wb") as ostream:
                for page in range(startpage, endpage):
                  outPdf.add_page(inputPdf.pages[page])
                  outPdf.write(ostream)
            return 0
        except:
            return 1
        finally:
            fileObject.close()
