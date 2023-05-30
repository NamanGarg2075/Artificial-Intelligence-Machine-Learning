from tkinter import *

root = Tk()

root.title("Title Changed")
root.geometry('500x500')
root.wm_iconbitmap('') # .ico file location

root.resizable(False,False) # Height and Width not resizeable

root.mainloop()