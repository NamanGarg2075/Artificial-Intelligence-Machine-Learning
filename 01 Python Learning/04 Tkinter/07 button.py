from tkinter import *

root = Tk()

def btnClick(): 
    clicked = Label(root, text="Button CLicked...")
    clicked.pack() 

btn = Button(root, text='Hello World!', command=btnClick)
btn.pack(padx=100,pady=100)

root.mainloop()