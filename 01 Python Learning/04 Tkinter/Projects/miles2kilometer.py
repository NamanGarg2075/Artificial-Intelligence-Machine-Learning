import tkinter as tk
from tkinter import ttk 

window = tk.Tk()
window.title("Miles2Kilo")
window.geometry('300x150')

# title 
title_label = ttk.Label(master=window,text="Miles 2 Kilometer", font=("Calibri 25 bold"))
title_label.pack()

def convert():
    miles_input = entry_int.get()
    km_output = miles_input * 1.61
    output_str.set("Kilometer: " + str(km_output))

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame,textvariable=entry_int)
btn = ttk.Button(master=input_frame,text='Convert', command=convert)
entry.pack(side='left',padx=10)
btn.pack(side='left')
input_frame.pack(pady=10)

# output
output_str = tk.StringVar()
output_label = ttk.Label(master=window,text="Output",textvariable=output_str)
output_label.pack()

window.mainloop()