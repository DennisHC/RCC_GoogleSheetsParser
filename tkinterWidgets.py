from tkinter import *
from tkinter import ttk
import gspreadFunctions as my_gspread
import fileIO as fio
import config

# GOOGLE_SHEETS_FILENAME
def google_sheets_filename_widget(root):
    ttk.Label(root, text = "What is the spreadsheet name?:").pack()
    spreadsheet_name = StringVar()
    spreadsheet_name.trace_add("write", my_gspread.retrieve_spreadsheet_name)
    spreadsheet_name_entry = Entry(root, width = 50, textvariable = spreadsheet_name)
    spreadsheet_name_entry.pack()

# CELL_COL
def cell_column_widget(root):
    ttk.Label(root, text = "Which column are we modifying? (Enter a letter):").pack()
    cell_col = StringVar()
    cell_col.trace_add("write", my_gspread.retrieve_cell_col)
    cell_col_entry = Entry(root, width = 8, textvariable = cell_col)
    cell_col_entry.pack()

# CELL_CONTENT
def cell_content_widget(root):
    ttk.Label(root, text = "How many points do you want to input:").pack()
    cell_content = StringVar()
    cell_content.trace_add("write", my_gspread.retrieve_cell_content)
    cell_content_entry = Entry(root, width = 8, textvariable = cell_content)
    cell_content_entry.pack()

# FULL NAMES TO ADD TO INPUT FILE
def member_names_widget(root):
    ttk.Label(root, text = "Please input names of members who attended this meeting:").pack()
    input_file_textbox = Text(root, height = 30, width = 20)
    input_file_textbox.pack()
    submit_button = ttk.Button(root, text = 'Submit Names', command = fio.retrieveInputForTextFile)
    submit_button.pack()

# entries_changed message/label
def entries_changed_widget(root):
    entries_changed_counter = StringVar()
    entries_changed_counter.set("0 cells have been updated so far.")
    entries_changed_label = Label(root, textvariable = entries_changed_counter)
    entries_changed_label.pack()

# errors_occured message/label
def errors_encountered_widget(root):
    errors_occured_counter = StringVar()
    errors_occured_counter.set("0 errors have occured so far.") 
    errors_occured_label = Label(root, textvariable = errors_occured_counter)
    errors_occured_label.pack()

# progress message
def progress_message_widget(root):
    progress_message = StringVar()
    progress_message.set("Thanks for using my application! -Dennis") 
    progress_message_label = Label(root, textvariable = progress_message)
    progress_message_label.pack()

# SUBMIT CHANGES TO GSPREADSHEET
def final_submission_widget(root):
    final_submission_button = ttk.Button(root, text = 'Submit Changes!', command = fio.makeChangesToSpreadsheet)
    final_submission_button.pack()