import os
import glob
from PyPDF2 import PdfFileMerger, PdfFileReader


def merger2(output_path, input_paths):
    pdf_merger = PdfFileMerger()
    file_handles = []
    for path in input_paths:
        pdf_merger.append(path)
    with open(output_path, 'wb') as fileobj:
        pdf_merger.write(fileobj)

files = os.listdir('D:/Study/Vidyamandir/Workbook PDF/Chemistry')
print(files)
for x in files:
    print(x)
    paths = glob.glob('D:/Study/Vidyamandir/Workbook PDF/Chemistry/'+ x +'/*.pdf')
    paths =sorted(paths)
    merger2('D:/Study/Vidyamandir/Workbook PDF/Chemistry/'+ x +'.pdf', paths)



    """date = []

    for i in paths:
        pdf = PdfFileReader(open(str(i), 'rb'))
        print(pdf.getDocumentInfo())
        try:
            date.append(pdf.getDocumentInfo()['/ModDate'])
        except:
            date.append(pdf.getDocumentInfo()['/CreationDate'])
    print(date)

    final_path = []

    while len(paths) > 0:
        print(date)
        print("running while")
        for i in paths:
            print("Running for 1")
            pdf = PdfFileReader(open(str(i), 'rb'))
            if len(date) > 0:
                try:
                    print("loop 1, try")
                    if pdf.getDocumentInfo()['/ModDate'] == min(date):
                        final_path.append(i)
                        date.remove(min(date))
                        paths.remove(i)
                        print("loop 1,try if")
                except:
                    pass
        for i in paths:
            final_path.append(i)
            paths.remove(i)
            print("loop 2")

    print(final_path)
"""