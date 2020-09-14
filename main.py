# Google Spreadsheet Libraries
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# GUI Libraries
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedStyle

# Regular Expressions Libary
import re

# File Flush
import os 

# My Libararies
import tkinterFunctions as my_tk
import gspreadFunctions as my_gspread
import tkinterWidgets as my_tk_widgets

# Global Variables
import config
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open(config.GOOGLE_SHEETS_FILENAME).sheet1

# Initialize Tkinter GUI Window
root = Tk()
root.title("UCI RCC Google Sheets Parser")
style = ThemedStyle(root)
style.set_theme("clearlooks")

# Clear/erase input.txt File
fp = open("input.txt", "w+")
fp.seek(0)
fp.truncate()
fp.close()

# Variables GLobal
progress_message = StringVar()

# GOOGLE_SHEETS_FILENAME
my_tk_widgets.google_sheets_filename_widget(root)

# CELL_COL
my_tk_widgets.cell_column_widget(root)

# CELL_CONTENT
my_tk_widgets.cell_content_widget(root)

# FULL NAMES TO ADD TO INPUT FILE
my_tk_widgets.member_names_widget(root)

# entries_changed message/label
my_tk_widgets.entries_changed_widget(root)

# errors_occured message/label
my_tk_widgets.errors_encountered_widget(root)

# progress message
my_tk_widgets.progress_message_widget(root)

# SUBMIT CHANGES TO GSPREADSHEET
my_tk_widgets.final_submission_widget(root)

root.mainloop()

try:
    root.destroy()
except:
    pass