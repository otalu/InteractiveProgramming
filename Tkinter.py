from tkinter import *
from tkinter import messagebox


top = Tk()

top.geometry("1000x1000")

def helloCallBack():
    msg = messagebox.showinfo("Hello Python", "Hello World")

A = Button(top, text = "Paris", command = helloCallBack)
A.place(x = 5, y = 500)
B = Button(top, text = "Berlin", command = helloCallBack)
B.place(x = 500, y = 500)
C = Button(top, text = "New Delhi", command = helloCallBack)
C.place(x = 50, y = 50)
D = Button(top, text = "Ankara", command = helloCallBack)
D.place(x = 50, y = 500)
top.mainloop()
