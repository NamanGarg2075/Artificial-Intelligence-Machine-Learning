from tkinter import *

root = Tk()

label_top = Label(root, text='Hello World!')
label_top.pack(side=TOP)

label_left = Label(root, text='Hello World!')
label_left.pack(side=LEFT)

label_bottom = Label(root, text='Hello World!')
label_bottom.pack(side=BOTTOM)

label_right = Label(root, text='Hello World!')
label_right.pack(side=RIGHT)

root.mainloop()