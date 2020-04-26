from tkinter import *
import tkinter.messagebox

class MainWindow:
    def __init__(self, master):
        self.master=master
        self.master.title("test")
        self.master.geometry('1350x750')
        self.master.title("Hotel Management System")
        self.master.config(bg='powder blue')

        #======================================Frames============================================================

        frame=Frame(self.master)
        frame.grid()

        mainframe=Frame(frame)
        mainframe.pack(side=LEFT)

        sideframe=Frame(frame)
        sideframe.pack(side=RIGHT)

        topframe=Frame(mainframe, bd=14, bg='powder blue', relief='ridge', height=120, width=1100, padx=400, pady=5)
        topframe.pack(side=TOP)

        midframe = Frame(mainframe, bd=14, bg='powder blue', relief='ridge', height=100, width=1080, pady=10, padx=10)
        midframe.pack(side=BOTTOM)

        leftframe = Frame(midframe, bd=14, bg='cadet blue', relief='ridge', height=590, width=680,)
        leftframe.pack(side=LEFT)

        rightframe = Frame(midframe, bd=14, bg='cadet blue', relief='ridge', height=590, width=380)
        rightframe.pack(side=RIGHT)

        buttonframe=Frame(sideframe, bd=14, bg='powder blue', relief='ridge', height=740, width=240, padx=10, pady=150)
        buttonframe.pack(side=RIGHT)

        #=======================================Widgits============================================================

        self.lblwelcome=Label(topframe, text='WELCOME', bg='powder blue', font='times 36 bold').pack()

        #=======================================Functions=========================================================

        def exit():
            iexit= tkinter.messagebox.askyesno('Hotel System','Confirm, If you Want to exit?')
            if iexit>0:
                root.destroy()
                return


        #======================================Buttons============================================================

        self.btn1 = Button(buttonframe, bd=4, text='Show Bookings', height=2, width=13, font='arial 16 bold',
                           activebackground="pink", activeforeground="dark blue").grid(row=0, column=0, pady=6)

        self.btn2 = Button(buttonframe, bd=4, text='Submit', height=2, width=13, font='arial 16 bold',
                           activebackground="pink", activeforeground="dark blue").grid(row=1, column=0, pady=6)

        self.btn3 = Button(buttonframe, bd=4, text='Clear', height=2, width=13, font='arial 16 bold',
                           activebackground="pink", activeforeground="dark blue").grid(row=2, column=0, pady=6)

        self.btn4 = Button(buttonframe, bd=4, text='Cancel', height=2, width=13, font='arial 16 bold',
                           activebackground="pink", activeforeground="dark blue").grid(row=3, column=0, pady=6)

        self.btn5 = Button(buttonframe, bd=4, text='Exit', height=2, width=13, font='arial 16 bold',
                           activebackground="pink", activeforeground="dark blue", command=exit).grid(row=4, column=0, pady=6)



if __name__ == '__main__':
    root=Tk()
    application=MainWindow(root)
    root.mainloop()