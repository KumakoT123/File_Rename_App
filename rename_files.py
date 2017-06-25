#!/usr/bin/env python
import tkinter as tk


class FileManager(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #Create simple layout that includes opening file manager and selecting
        #respective files
        self.helperTxt = tk.Label(self, text="Select your files and decide your name")
        self.helperTxt.pack()

        vcmd = self.register(self.check_user_input)
        self.file_name_entry = tk.Entry(self, validate="key", validatecommand=(vcmd, '%P'))
        self.file_name_entry.pack()
        
        self.rename_btn = tk.Button(self, text="Rename", command=self.rename_files)
        self.rename_btn.pack()


    def check_user_input(self, file_name):
        #validate proper file naming
        print("Input checked")
        return True

    def rename_files(self):
        #rename file code
        print("Rename files")

    def select_files(self):
        #Get files from file directory

root = tk.Tk()
root.resizable(width=False, height=False)
root.minsize(600, 450)

my_gui = FileManager(root)
my_gui.master.title("Rename files")


root.mainloop()
