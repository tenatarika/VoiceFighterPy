from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import  LAParams
from io import  StringIO
from io import  open 

def convent(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    
    process_pdf(rsrcmgr, device, pdfFile)
    device.close()
    
    content = retstr.getvalue()
    retstr.close()
    
    return content


def read_pdf_from_url(url):
    pdfFile = urlopen(url)
    outputString = convent(pdfFile)
    pdfFile.close()
    return outputString

def read_pdf_from_file(path):
    pdfFile = open(path, 'rb')
    outputString = convent(pdfFile)
    pdfFile.close()
    return outputString
    
    