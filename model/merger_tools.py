from PyPDF2 import PdfWriter, PdfReader, PdfMerger


class Marger:
    def merge_pdf(self,files):
        try:
            merger = PdfMerger()
            for file in files:
                print(file)
                merger.append(file)
            merger.write('merged.pdf')
            return 0
        except:
            return 1
        finally:
            merger.close()


