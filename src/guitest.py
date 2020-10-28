from __future__ import division
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog

class MainWindow(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("FOO converter")
        self.master.minsize(350, 150)
        self.grid(sticky=E+W+N+S)

        self.save_dir = None
        self.filename_open = None

        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

        self.CHART_FILE_TYPES = [('Pentax Electronic Format', '*.pef'),
                                ('Sony Alpha Raw', '*.arw'),
                                ('Minolta Raw', '*.mrw'),
                                ('Camera Image File Format', '*.crw'),
                                ('Canon Raw', '*.cr2'),
                                ('Epson Raw', '*.erw'),
                                ('Samsung Raw', '*.srw'),
                                ('Fujifilm Raw', '*.raf'),
                                ('Kodak Digital Camera Raw', '*.dcr'),
                                ('Nikon Electronic Format', '*.nef'),
                                ('Olympus Raw', '*.orf'),
                                ('All files', '.*')]

        for i in range(10): self.rowconfigure(i, weight=1)
        self.columnconfigure(1, weight=1)

        self.open = Button(self, text='Input raw image file', command=self.open, activeforeground="red")
        self.open.grid(row=0, column=0, pady=2, padx=2, sticky=E+W+N+S)

        self.sep = Frame(self, height=2, width=450, bd=1, relief=SUNKEN)
        self.sep.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

        self.CheckVar_camera_white_balance = IntVar()
        self.CheckVar_camera_white_balance = Checkbutton(self,
            text="Camera white balance",
            variable=self.CheckVar_camera_white_balance,
            onvalue=1,
            offvalue=0)
        self.CheckVar_camera_white_balance.grid(row=2, column=0, pady=0, padx=0, sticky=W)

        self.CheckVar_average_whole_image_white_balance = IntVar()
        self.CheckVar_average_whole_image_white_balance = Checkbutton(self,
            text="Average the whole image for white balance",
            variable=self.CheckVar_average_whole_image_white_balance,
            onvalue=1,
            offvalue=0)
        self.CheckVar_average_whole_image_white_balance.grid(row=3, column=0, pady=0, padx=0, sticky=W)

        self.CheckVar_correct_chromatic_aberration = IntVar()
        self.CheckVar_correct_chromatic_aberration = Checkbutton(self,
            text="Correct chromatic aberration",
            variable=self.CheckVar_correct_chromatic_aberration,
            onvalue=1,
            offvalue=0)
        self.CheckVar_correct_chromatic_aberration.grid(row=4, column=0, pady=0, padx=0, sticky=W)

        self.CheckVar_fix_dead_pixels = IntVar()
        self.CheckVar_fix_dead_pixels = Checkbutton(self,
            text="Fix dead pixels",
            variable=self.CheckVar_fix_dead_pixels,
            onvalue=1,
            offvalue=0)
        self.CheckVar_fix_dead_pixels.grid(row=5, column=0, pady=0, padx=0, sticky=W)

        self.sep = Frame(self, height=2, width=450, bd=1, relief=SUNKEN)
        self.sep.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

        self.CheckVar_brightness = IntVar()
        self.CheckVar_brightness = Checkbutton(self, text="Brightness",
            command=self.switch_brightness,
            variable=self.CheckVar_brightness,
            onvalue=1,
            offvalue=0)
        self.CheckVar_brightness.grid(row=7, column=0, pady=0, padx=2, sticky=W)

        self.label_level_brightness = Label(self, text="Brightness level:", state=DISABLED)
        self.label_level_brightness.grid(row=8, column=0, pady=0, padx=0, sticky=W)

        self.entry_level_brightness = Entry(self, state=DISABLED)
        self.entry_level_brightness.grid(row=8, column=1, pady=0, padx=0, sticky=W)

        self.label_gamma_curve = Label(self, text="Gamma curve:", state=DISABLED)
        self.label_gamma_curve.grid(row=9, column=0, pady=0, padx=0, sticky=W)

        self.entry_gamma_curve_1 = Entry(self, state=DISABLED)
        self.entry_gamma_curve_1.grid(row=9, column=1, pady=0, padx=0, sticky=W)

        self.entry_gamma_curve_2 = Entry(self, state=DISABLED)
        self.entry_gamma_curve_2.grid(row=9, column=2, pady=0, padx=0, sticky=E+W+N+S)


# functions

    def open(self):
        self.filename_open = tkFileDialog.askopenfilename(filetypes=self.CHART_FILE_TYPES, defaultextension='.*')

    def switch_brightness(self):
        pass

if __name__ == "__main__":
   d = MainWindow()
   d.mainloop()