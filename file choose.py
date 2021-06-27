from tkinter import Tk
from tkinter.filedialog import askdirectory, asksaveasfile

Tk().withdraw()
filename = asksaveasfile(mode='wb')
print(filename)
