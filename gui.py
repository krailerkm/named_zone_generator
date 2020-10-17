import tkinter as tk

def set_message():
    text = text_input.get()
    title_label.configure(text=text)

windows = tk.Tk()
windows.title('JustPython')
windows.minsize(width=400, height=400)

title_label = tk.Label(master=windows, text='Hello world')
title_label.pack()

text_input = tk.Entry(master=windows)
text_input.pack()

ok_button = tk.Button(master=windows, text='Ok', command=set_message)
ok_button.pack()

windows.mainloop()