from tkinter import *

class win1:
    def __init__(self,master):
        self.master=master
        self.master.title("test")
        self.master.geometry('750x750')
        self.master.title("hello")
        self.frame=Frame(self.master)
        self.frame.pack()
root = Tk()
app=win1(root)
print("working")
mainloop()

"""class window():
    def __init__(self, win_nm, geo, title):
        self.win_nm=Tk()
        self.win_nm.title(title)
        self.win_nm.geometry(geo)
    def open(self):
        self.win_nm.mainloop()
    
W1= window('1','400x180','hello')

W2.open()"""
"""
class cars:
    def __init__(self,price,year):
        self.price=price
        self.year=year
    def inc(self):
        self.year+=2
swift=cars(2000000,2005)
dzire=cars(3000000,2007)
print(swift.__dict__,dzire.__dict__)
dzire.inc()
print(swift.__dict__,dzire.__dict__)
"""
