import os
import sys
import csv
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory

global_count = 0
global_long = 0
global_long_list = []
 
def listdirs(rootdir):
    global global_count
    global global_long
    global global_long_list

    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        d = d.replace('/', '\\')
        global_count += 1
        sys.stdout.write('\r')
        sys.stdout.write('[Directories scanned: ' + str(global_count))
        sys.stdout.write('  <<---->>  Long directories detected: ' + str(global_long))
        sys.stdout.write(']          ')
        sys.stdout.flush()
        if len(d) >= 256:
            global_long += 1
            global_long_list.append(d)
        if os.path.isdir(d):
            listdirs(d)

def gui():
    main = Tk()
    main.title('Configurator')
    def browse():
        global global_count
        global global_long
        global global_long_list

        global_count = 0
        global_long = 0
        global_long_list = []
        path = askdirectory()
        dir_ent.delete(0, END)
        dir_ent.insert(0, path)
    def save():
        global global_count
        global global_long
        global global_long_list

        global_count = 0
        global_long = 0
        global_long_list = []
        rootdir = dir_ent.get()
        if len(dir_ent.get()) == 0:
            messagebox.showinfo(title="Important message", message="Please select a reference file")
            return
        listdirs(rootdir)
        print(global_long_list)

    main.geometry('280x50')

    Label(main, text = "Root Dir:").grid(row=0, column=0)

    dir_ent = Entry(main)

    dir_ent.grid(row=0, column=1, columnspan=10, sticky=EW)
    Button(main, text='Browse', command=browse).grid(row=0, column=11, sticky=EW)

    Button(main, text='Scan', command=save, bg = "#5fb878").grid(row=1, column=12, sticky=EW)

    mainloop()

if __name__ == "__main__":
    gui()