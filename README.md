# 📂 File Organizer
A graphical user interface tool for automatically sorting files based on their extensions.
A clear and efficient desktop application built in Python, designed for instantly organizing folders. This tool automates the process of sorting cluttered directories into structured subfolders based on file categories.

## Features
- **Automated Sorting:** Automatically categorizes files into specific folders (Images, Documents, Videos, Music, Archives).
- **Modern Dark UI:** A sleek, user-friendly Dark Mode interface built with Python's Tkinter (ttk) library.
- **Smart Conflict Resolution:** Prevents data loss by automatically renaming files if a duplicate exists in the destination folder (e.g., `photo.jpg` becomes `photo_1.jpg`).
- **"Others" Catch-all:** Moves any unrecognized file types into a dedicated "Others" folder to ensure no file is left behind.
- **Safety First:** The script is programmed to ignore subdirectories and only manipulate individual files.

## Built With
- **Python** 3.10.17
- **Tkinter (ttk):** For the Graphical User Interface.
- **OS & Shutil:** For advanced file system manipulation and movement.

## Getting Started
1. Ensure you have **Python 3.10.17** installed on your machine.
2. Download the "file-organizer.py" file.
3. Open your terminal or command prompt and navigate to the folder containing the file.
4. Run the application:
   ```bash
   python file-organizer.py
