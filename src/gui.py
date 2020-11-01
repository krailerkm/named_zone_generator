#!/usr/bin/python
#import tkinter as tk

#def set_message():
#    text = text_input.get()
#    title_label.configure(text=text)

#windows = tk.Tk()
#windows.title('JustPython')
#windows.minsize(width=400, height=400)

#title_label = tk.Label(master=windows, text='Hello world')
#title_label.pack()

#text_input = tk.Entry(master=windows)
#text_input.pack()

#ok_button = tk.Button(master=windows, text='Ok', command=set_message)
#ok_button.pack()

#windows.mainloop()

from tkinter import tix as tx

root=tx.Tk()
root.geometry("800x600+0+10")

swr=tx.ScrolledWindow(root)
swr.pack(fill=tx.BOTH, expand=1)

nb=tx.NoteBook(swr.window)
nb.pack(fill=tx.BOTH, expand=1)

for i in range(1,3):
	nb.add("tab"+str(i),label="Tab "+str(i))

for k in range(1,39):
	l=tx.Label(nb.tab1,text="label "+str(k))
	l.pack()

for k in range(1,29):
	l=tx.Label(nb.tab2,text="label "+str(k))
	l.pack(side=tx.LEFT)

root.mainloop()