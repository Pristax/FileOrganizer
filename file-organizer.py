#======================================================================
# Project: File Organizer
# Author: Pristax
# Year: 2026
# Description: GUI tool for automatic file sorting based on extensions.
#======================================================================

import os
import shutil
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showerror
from tkinter.ttk import *
from tkinter import filedialog

EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"]
}

class fileOrganizer(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master=master)
        self.selected_path = ""

        self.master.configure(bg="#2d2d2d")
        self.configure(style="TFrame")
        
        self.setup_styles()

        self.Application()
        self.pack(expand=True, fill="both", padx=20, pady=20)

    def setup_styles(self):
        style = Style()
        style.theme_use('clam')
        
        style.configure("TFrame", background="#2d2d2d")
        
        style.configure("TLabel", 
                        background="#2d2d2d", 
                        foreground="#ffffff", 
                        font=("Segoe UI", 10))
        
        style.configure("TButton", 
                        padding=10, 
                        font=("Segoe UI", 10, "bold"),
                        background="#3d3d3d",
                        foreground="#ffffff")
        
        style.configure("Accent.TButton", 
                        background="#0078d7", 
                        foreground="#ffffff")
        style.map("Accent.TButton", background=[('active', '#005a9e')])

    def Application(self):
        self.title_label = Label(self, text="FILE ORGANIZER", font=("Segoe UI", 16, "bold"))
        self.title_label.pack(pady=(0, 20))

        self.btn_select = Button(self, text="Select folder", command=self.buttonAction)
        self.btn_select.pack(pady=5, fill="x")

        self.path_label = Label(self, text="No folder selected", wraplength=350)
        self.path_label.pack(pady=5)

        self.btn_running = Button(self, text="Organize files", command=self.organizeAction, style="Accent.TButton")
        self.btn_running.pack(pady=10, fill="x")

    def buttonAction(self):
        path = filedialog.askdirectory()
        if path:
            self.selected_path = path
            self.path_label.config(text=f"Selected: {path}")
            print(f"Path saved: {self.selected_path}")

    def organizeAction(self):
        if not self.selected_path:
            showerror("Error", "No path selected!")
            return
        
        for filename in os.listdir(self.selected_path):
            filepath = os.path.join(self.selected_path, filename)
        
            if os.path.isdir(filepath):
                continue
                
            extension = os.path.splitext(filename)[1].lower()
            found_category = False
            
            target_folder_name = "Others"
            for folder_name, ext_list in EXTENSIONS.items():
                if extension in ext_list:
                    target_folder_name = folder_name
                    found_category = True
                    break
            
            dest_folder = os.path.join(self.selected_path, target_folder_name)
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)

            final_dest = os.path.join(dest_folder, filename)
            if os.path.exists(final_dest):
                name, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(os.path.join(dest_folder, f"{name}_{counter}{ext}")):
                    counter += 1
                final_dest = os.path.join(dest_folder, f"{name}_{counter}{ext}")

            shutil.move(filepath, final_dest)
            print(f"Moved: {filename} -> {target_folder_name}")
                
        messagebox.showinfo("Done", "Files have been organized safely!")

root = Tk()
root.geometry("400x250")
root.title("File Organizer")
app = fileOrganizer(root)
app.mainloop()