from PyPDF2 import PdfWriter,PdfReader

def cropper(start,end,file):
    if(start !=  0):
        start -=1
    try:
        inputPdf = PdfReader(open(file,"rb"))
        if(start > len(inputPdf.pages) or end > len(inputPdf.pages) or start >= end):
            return len(inputPdf.pages)
        outPdf = PdfWriter()
        with open(file.split(".")[0]+"cropped"+".pdf","wb") as ostream:
            for page in range(start, end):
              outPdf.add_page(inputPdf.pages[page])
              outPdf.write(ostream)
        return 0
    except:
        return 1