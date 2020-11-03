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
from tkinter import *

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()

    def initUI(self):      
        self.parent.title("NCG v1.0a - (Named configuration generator version 1.0a)")

        Label(text="Contact List").grid(row=0,column=0,columnspan=2)
        Text(width=30,height=22).grid(row=1,rowspan=9, column=0,columnspan=2,padx=20)

        Button(text="Generate >>").grid(row=5, column=2,columnspan=1,pady=10)

        Label(text="Generate Contact").grid(row=0,column=3,columnspan=2)
        Text(width=30,height=22).grid(row=1,rowspan=9, column=3,columnspan=2,padx=20)

def main():
    root = Tk()
    root.geometry("650x400+900+300")
    root.resizable(0,0)
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  