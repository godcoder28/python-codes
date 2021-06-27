from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter.filedialog import askopenfile
writer = PdfFileWriter()
Tk().withdraw()
file = askopenfile(mode='rb')
reader = PdfFileReader(file, strict=False)
for page in reader.pages:
    if 
