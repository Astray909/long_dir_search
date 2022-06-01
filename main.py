import os
import sys
import csv
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory

global_count = 0
global_long = 0
global_long_list = []
 
def listdirs(rootdir, max_len):
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
        if len(d) >= max_len:
            global_long += 1
            global_long_list.append([d])
        if os.path.isdir(d):
            listdirs(d, max_len)

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
            messagebox.showinfo(title="Important message", message="Please select a root directory")
            return
        if len(len_ent.get()) == 0:
            messagebox.showinfo(title="Important message", message="Please enter max length")
            return
        try:
            test = int(len_ent.get())
        except:
            messagebox.showinfo(title="Important message", message="Please enter an integer instead")
            return
        listdirs(rootdir, int(len_ent.get()))
        with open('output.csv', 'w', newline='') as f:
            write = csv.writer(f)
            write.writerows(global_long_list)
        f.close()
    def reset():
        len_ent.delete(0, END)
        len_ent.insert(0, 256)

    main.geometry('280x50')

    Label(main, text = "Root Dir:").grid(row=0, column=0)
    Label(main, text = "Max length:").grid(row=1, column=0)

    dir_ent = Entry(main)
    len_ent = Entry(main)

    dir_ent.grid(row=0, column=1, columnspan=10, sticky=EW)
    len_ent.grid(row=1, column=1, columnspan=10, sticky=EW)

    reset()

    Button(main, text='Browse', command=browse).grid(row=0, column=11, sticky=EW)
    Button(main, text='Reset', command=reset).grid(row=1, column=11, sticky=EW)
    Button(main, text='Scan', command=save, bg = "#5fb878").grid(row=1, column=12, sticky=EW)

    mainloop()

if __name__ == "__main__":
    gui()