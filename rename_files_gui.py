#!/usr/bin/env python
import tkinter as tk
import subprocess
import glob, os


class FileManager(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #Create simple layout that includes opening file manager and selecting
        #respective files

        self.errorTxt = tk.Label(self, fg="red")
        self.errorTxt.pack()

        vcmd_file_name = self.register(self.check_file_input)
        option_file_name = {'validate' : 'key', 'validatecommand' : "(vcmd_file_name, '%P')"}
        self.file_name_entry = self.make_entry("Enter file name", 10, **option_file_name)

        self.search_files_btn = tk.Button(self, text="Search Files", command=self.select_files)
        self.search_files_btn.pack()
        
        vcmd_name_input = self.register(self.check_name_input)
        option_name_input = {'validate' : 'key', 'validatecommand' : "(vcmd_name_input), '%P')"}
        self.output_file_entry = self.make_entry("Enter desired file name", 10, **option_name_input)
        
        self.rename_btn = tk.Button(self, text="Rename", command=self.rename_files)
        self.rename_btn.pack()


    def check_file_input(self, P:
        #validate proper file naming
        print("Input checked")
        return True

    def check_name_input(self, P):
        #validate
        print("Output name")
        return True

    def rename_files(self):
        #rename file code
        print("Rename files")

    def select_files(self):
        #Get files from file directory
        file_to_show = "/Documents"
        subprocess.call(["open", "-R", file_to_show])
        print("Files selected")

    def make_entry(self, caption, width=None, **options):
        tk.Label(self, text=caption).pack()
        entry = tk.Entry(self, **options)
        if width:
            entry.config(width=width)
        entry.pack()
        return entry


root = tk.Tk()
root.resizable(width=False, height=False)
root.minsize(600, 450)

my_gui = FileManager(root)
my_gui.master.title("Rename files")


root.mainloop()
