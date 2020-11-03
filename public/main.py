#!/usr/bin/python
# -*- coding: utf-8 -*-
# 3 November 2020 Codeing by Krailerk M.
# This script for convert txt list of url to named new zone for block in pdns
# NCG v1.0a - (Named configuration generator version 1.0a) 
#  _____         _ _         _      _____   
# |  |  |___ ___|_| |___ ___| |_   |     |  
# |    -|  _| .'| | | -_|  _| '_|  | | | |_ 
# |__|__|_| |__,|_|_|___|_| |_,_|  |_|_|_|_|
#                                           
#
import tkinter as tk
import tkinter.scrolledtext as st 

def main():
    win = tk.Tk()
    win.title("NCG v1.0a - (Named configuration generator version 1.0a)")
    win.geometry("680x400+900+300")
    win.resizable(0,0)

    tk.Label(text="Contact List").grid(row=0,column=0,columnspan=2)

    text1 = st.ScrolledText(win,width=30,height=22) 
    text1.grid(row=1,rowspan=9, column=0,columnspan=2,padx=20)

    tk.Button(text="Generate >>").grid(row=5, column=2,columnspan=1,pady=10)

    tk.Label(text="Generate Contact").grid(row=0,column=3,columnspan=2)

    text2 = st.ScrolledText(win,width=30,height=22) 
    text2.grid(row=1,rowspan=9, column=3,columnspan=2,padx=20)


    win.mainloop()  


if __name__ == '__main__':
    main()  