import glob
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory, asksaveasfile

from PyPDF2 import PdfFileReader, PdfFileWriter

Tk().withdraw()
folder = askdirectory()

Tk().withdraw()
output = asksaveasfile(mode="wb")

choice = input("Delete previous files? ")
paths = glob.glob(folder + '\*.pdf')


def pdf_merge(inputs: [str], output: str, delete: bool = False):
    """
    Merge multiple Pdf input files in one output file.
    :param inputs: input files
    :param output: opened output file
    :param delete: delete input files after completion if true

    """
    writer = PdfFileWriter()
    try:
        infiles = []
        for filename in inputs:
            f = open(filename, "rb")
            reader = PdfFileReader(f, strict=False)
            for page in reader.pages:
                writer.addPage(page)
            infiles.append(f)
        writer.write(output)
    except FileNotFoundError as e:
        print(e.strerror + ": " + e.filename)
    finally:
        output.close()
        for f in infiles:
            f.close()
    if delete:
        for filename in inputs:
            os.remove(filename)
        try:
            os.removedirs(folder)
        except:
            pass


pdf_merge(paths, output)
