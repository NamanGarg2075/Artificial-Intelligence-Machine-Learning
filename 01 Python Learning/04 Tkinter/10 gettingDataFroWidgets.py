import tkinter as tk 
from tkinter import ttk

def btn_func():
    # get data of entry widget
    print(entry.get())

    # update the label

    # label.config(text=entry.get())
    # label.configure(text=entry.get())
    label['text'] = entry.get()
    entry['state'] ='disabled' # disable entry widget after updation


# window
window = tk.Tk()
window.title("Getting Data")

# widgets
label = ttk.Label(master=window,text="Label")
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window,text='GET DATA',command= btn_func)
button.pack()

# run
window.mainloop()