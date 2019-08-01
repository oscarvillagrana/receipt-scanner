#!/usr/bin/python


#-------------------------------------------------------
# Here I want to read PDFs to turn scanned receipts 
# into a pandas dataframe
#-------------------------------------------------------



# from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content

# pdfFile = urlopen("http://.pdf");
pdfFile = open(input("Enter a file to read: "));
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()


#-------------------------------------------------------------------
# Now I need to turn this output and parse it into tables using tags
# i.e. store, item, price, quantity
#-------------------------------------------------------------------
