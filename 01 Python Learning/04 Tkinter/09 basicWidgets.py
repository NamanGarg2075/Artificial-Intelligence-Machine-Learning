import tkinter as tk
from tkinter import ttk

# create a window
window = tk.Tk()
window.title('Widgets')
window.geometry('800x500')

# create widgets
text=tk.Text(master=window)
text.pack()

# ttk label
label = ttk.Label(master=window,text="Hgfdfghjk")
label.pack()

# ttk entry
entry = ttk.Entry(master=window)
entry.pack()

# ttk button
btn = ttk.Button(master=window,text='CLICK ME')
btn.pack()

# run
window.mainloop()