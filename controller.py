from tkinter.messagebox import *
from tkinter import filedialog

def ruta():
    folder_selected = filedialog.askdirectory()
    return folder_selected