from tkinter import Tk
from tkinter.filedialog import askopenfile, asksaveasfile

from PyPDF2 import PdfFileReader, PdfFileWriter

Tk().withdraw()
file = askopenfile(mode="rb")

Tk().withdraw()
output = asksaveasfile(mode="wb")
list = [22]
writer = PdfFileWriter()
try:
    reader = PdfFileReader(file, strict=False)
    for page in reader.pages:
        if reader.getPageNumber(page)+1 not in list:
            writer.addPage(page)
    writer.write(output)
except FileNotFoundError as e:
    print(e.strerror + ": " + e.filename)
finally:
    output.close()
    file.close()
