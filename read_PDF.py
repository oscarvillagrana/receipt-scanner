#!/usr/bin/python
# Web Scraping With Python. pg.101

#-------------------------------------------------------
# Reading a PDF in preperation to turn scanned reciepts
# into a database for analysis
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

pdfFile = open(input("Enter a file to read: "))
# pdfFile = urlopen("http://.pdf");
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()

