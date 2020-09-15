# Google Spreadsheet Libraries
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# GUI Libraries
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedStyle

# Global Variables
import config

# My Modules
import tkinterWidgets as my_tk_widgets
import fileIO

# Initialize Tkinter GUI Window
Frame = Tk()
Frame.title("UCI RCC Google Sheets Parser")
style = ThemedStyle(Frame)
style.set_theme("clearlooks")

# Clear/erase input.txt file before use
fileIO.clear_file("input.txt")

# Create UI
my_tk_widgets.MakeUI(Frame)
Frame.iconphoto(False, PhotoImage(file='rcc_logo.png'))

Frame.mainloop()

try:
    Frame.destroy()
except:
    pass