from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import glob

folder = input("Enter Path of Folder Containg pdfs: ")
output = input("Enter Path of Output file: ")
choice = input("Delete previous files? ")
paths = glob.glob(folder)

def pdf_merge(inputs: [str], output: str, delete: bool = False):
    """
    Merge multiple Pdf input files in one output file.
    :param inputs: input files
    :param output: output file
    :param delete: delete input files after completion if true

    """
    writer = PdfFileWriter()
    if os.path.isfile(output):
        ans = input(
            "The file '%s' already exists. "
            "Overwrite? Yes/Abort [Y/a]: " % output
        ).lower()
        if ans == "a":
            return

    outputfile = open(output, "wb")
    try:
        infiles = []
        for filename in inputs:
            f = open(filename, "rb")
            reader = PdfFileReader(f)
            for page in reader.pages:
                writer.addPage(page)
            infiles.append(f)
        writer.write(outputfile)
    except FileNotFoundError as e:
        print(e.strerror + ": " + e.filename)
    finally:
        outputfile.close()
        for f in infiles:
            f.close()
    if delete:
        for filename in inputs:
            os.remove(filename)
print(paths,output)

#pdf_merge(paths, output)
