import os
from tkinter import messagebox


# »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
# UPDATE WINDOWS 11 MENU
# This code makes it so that every time you right click in
# windows 11 it automatically goes to the "show more options"
# menu rather than the annoying simplified one.
# »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
try:
    os.system('reg add "HKCU\\Software\\Classes\\CLSID\\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\\InprocServer32" /f /ve')
    messagebox.showinfo("Command Complete", "The code has run successfully. In order for it to take affect, please restart your device.")

except Exception as e:
    messagebox.showerror("There was an error running the code", f"Error Message:\n{e}")
