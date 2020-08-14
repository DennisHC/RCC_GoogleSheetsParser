# Google Spreadsheet Libraries
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# GUI Libraries
from tkinter import *
from tkinter import ttk

# Regular Expressions Libary
import re

# File Flush
import os 

# My Libararies
# import tkinterFunctions as myTk
# import gspreadFunctions as myGSpread

# Global Variables
CELL_COL = "B"
CELL_CONTENT = "1"
GOOGLE_SHEETS_FILENAME = "Google Sheets Parser Test"

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open(GOOGLE_SHEETS_FILENAME).sheet1

# Initialize Tkinter GUI Window
root = Tk()
root.title("UCI RCC Google Sheets Parser")

# Clear/erase input.txt File
fp = open("input.txt", "w+")
fp.seek(0)
fp.truncate()
fp.close()

# Tkinter Command Functions
def retrieve_spreadsheet_name(self, *args):
    global GOOGLE_SHEETS_FILENAME
    GOOGLE_SHEETS_FILENAME = spreadsheet_name.get()

# New implementation: Inputting Letters
def retrieve_cell_col(self, *args):
    global CELL_COL
    temp = cell_col.get()
    temp = temp.upper()
    result = 0

    for i, T, in enumerate(temp[::-1]):
        letterNumber = ord(T) - ord("A") + 1
        result += letterNumber * (26 ** i)
    CELL_COL = result

def retrieve_cell_content(self, *args):
    global CELL_CONTENT
    CELL_CONTENT = cell_content.get()

# onButton 
def retrieveInputForTextFile():
    inputValue = inputFileTextBox.get("1.0", "end-1c")
    # Open file i/o
    try:
        fp = open("input.txt", "w")
    except:
        # print("File to open does not exist!")
        progress_message.set("Failed to open input.txt, file does not exist!")
    fp.write(inputValue) # Write to input.txt file
    # fp.write("\n")

    # Commands for real-time updating input.txt file
    fp.flush()
    os.fsync(fp.fileno())

    # print(inputValue) # Debugging/Printing to Console
    inputFileTextBox.delete(1.0, END) # Clear's TextBox Widget on Success
    fp.close() # Close the file i/o

# Gspread Functions
def makeChangesToSpreadsheet():
    # Edge cases

    # Should not overwrite member names
    if CELL_COL == 1:
        progress_message.set("Invalid option, cannot update cells that contain member names.")
        return

    # Set Google Sheets
    try:
        sheet = client.open(GOOGLE_SHEETS_FILENAME).sheet1
    except:
        progress_message.set("Invalid Google Sheets Filename.")
        return


    # Attempt to open input.txt File
    try:
        fpr = open("input.txt", "r")
    except:
        print("File to open does not exist!")
    # Attempt to open error.txt File
    try:
        fpErr = open("error.txt", "w")
    except:
        print("Failed to open error.txt")

    name = fpr.readline().strip()

    # Variables to keep track of errors and progress
    entries_changed = 0
    errors = 0

    while name:
        try:
            nameRegex = re.compile(name, re.IGNORECASE)
            cell = sheet.find(nameRegex)
            # print(name)

            # print("Found something at R%s C%s" % (cell.row, cell.col))
            # print("Updating values B%s\n" % (cell.row))
            # ex.) B1 -> (Column + Row)

            
            sheet.update_cell(cell.row, CELL_COL, CELL_CONTENT) # Update the value of the current cell

            entries_changed += 1

            name = fpr.readline().strip() # Continue iterating through file
        except:
            # print("FAILED TO COMPUTE FOR: %s\n" % (name)) # Error Message for feedback
            fpErr.write("FAILED TO COMPUTE FOR: %s\n" % (name)) # Error Message for feedback to error.txt
            errors += 1
            name = fpr.readline().strip() # Continue iterating through file
            continue # Skip back to beginning of loop

    # Updating entries_changed label    
    # print(entries_changed)
    if (entries_changed == 1):
        entries_changed_counter.set("%s cell has been updated." % (entries_changed))
    else:
        entries_changed_counter.set("%s cells have been updated." % (entries_changed))
    
    # Updating errors_occurred label
    if (errors == 1):
        errors_occured_counter.set("%s error has occured." % (errors))
    else:
        errors_occured_counter.set("%s errors have occured." % (errors))

    # Updating progress_message label
    progress_message.set("Success!")

    # Close file i/o
    fpr.close()
    fpErr.close()

    # Print success message
    # print("input.txt file parsing completed")


# GOOGLE_SHEETS_FILENAME
ttk.Label(root, text="What is the spreadsheet name?:").pack()
spreadsheet_name = StringVar()
spreadsheet_name.trace_add("write", retrieve_spreadsheet_name)
spreadsheet_name_entry = Entry(root, width = 50, textvariable = spreadsheet_name)
spreadsheet_name_entry.pack()

# CELL_COL
ttk.Label(root, text="Which column are we modifying? (Enter a letter):").pack()
cell_col = StringVar()
cell_col.trace_add("write", retrieve_cell_col)
cell_col_entry = Entry(root, width = 8, textvariable = cell_col)
cell_col_entry.pack()

# CELL_CONTENT
ttk.Label(root, text="How many points do you want to input:").pack()
cell_content = StringVar()
cell_content.trace_add("write", retrieve_cell_content)
cell_content_entry = Entry(root, width = 8, textvariable = cell_content)
cell_content_entry.pack()

# FULL NAMES TO ADD TO INPUT FILE
ttk.Label(root, text="Please input names of members who attended this meeting:").pack()
inputFileTextBox = Text(root, height=30, width=20)
inputFileTextBox.pack()
submitButton = ttk.Button(root, text='Submit Names', command= retrieveInputForTextFile)
submitButton.pack()

##startframe = Frame(root)
#canvas = Canvas(root, width = 1000, height = 1000)
#canvas.pack()
#img = PhotoImage(master = canvas, file="rcc_logo.png", width = 1000, height = 1000)
#canvas.create_image(20,20, anchor = NW, image = img)
#PhotoImage(master = canvas, width = 20, height = 20)


# entries_changed message/label
entries_changed_counter = StringVar()
entries_changed_counter.set("0 cells have been updated so far.")
entries_changed_label = Label(root, textvariable=entries_changed_counter)
entries_changed_label.pack()

# errors_occured message/label
errors_occured_counter = StringVar()
errors_occured_counter.set("0 errors have occured so far.") 
errors_occured_label = Label(root, textvariable=errors_occured_counter)
errors_occured_label.pack()

# progress message
progress_message = StringVar()
progress_message.set("Thanks for using my application! -Dennis") 
progress_message_label = Label(root, textvariable=progress_message)
progress_message_label.pack()

# SUBMIT CHANGES TO GSPREADSHEET
finalSubmissionButton = ttk.Button(root, text='Submit Changes!', command = makeChangesToSpreadsheet)
finalSubmissionButton.pack()

root.mainloop()

try:
    root.destroy()
except:
    pass

# print("Dennis' Google Sheets Parser has finished running successfully.")