import PyPDF2
file = open(r'D:\Study\NCERT\Class-XII\Physics-II\15_Communication Systems.pdf','rb')
file2 = open(r'C:\Users\shiva\Desktop\file.txt', 'w', encoding='ansi')
reader = PyPDF2.PdfFileReader(file)
for i in range(reader.numPages):
    page = reader.getPage(i)
    x = page.extractText()
    file2.write(x.encode('ansi', 'replace').decode('ansi', 'replace'))
