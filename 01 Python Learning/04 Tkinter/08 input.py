from tkinter import *

root = Tk()

field = Entry(root,width='10',font=("cascadia code", 25))
field.pack(padx=50,pady=50)

def clickBtn():
    label = Label(root,text=field.get())
    label.pack()

btn = Button(root,text="CLICK ME",command=clickBtn)
btn.pack()

root.mainloop()