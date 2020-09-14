import re
import os
from tkinter import *
from tkinter import ttk
import config
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# onButton 
def retrieveInputForTextFile():
    input_value = input_file_textbox.get("1.0", "end-1c")
    # Open file i/o
    try:
        fp = open("input.txt", "w")
    except:
        # print("File to open does not exist!")
        progress_message.set("Failed to open input.txt, file does not exist!")
    fp.write(input_value) # Write to input.txt file

    # Commands for real-time updating input.txt file
    fp.flush()
    os.fsync(fp.fileno())

    # print(input_value) # Debugging/Printing to Console
    input_file_textbox.delete(1.0, END) # Clear's TextBox Widget on Success
    fp.close() # Close the file i/o

# Gspread Functions
def makeChangesToSpreadsheet():
    # Edge cases

    # Should not overwrite member names
    if config.CELL_COL == 1:
        progress_message.set("Invalid option, cannot update cells that contain member names.")
        return

    # Set Google Sheets
    try:
        sheet = client.open(config.GOOGLE_SHEETS_FILENAME).sheet1
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
        fp_err = open("error.txt", "w")
    except:
        print("Failed to open error.txt")
    
    if os.stat("input.txt").st_size == 0:
        progress_message.set("The input.txt file is empty! No changes were made.")
        return

    name = fpr.readline().strip()

    # Variables to keep track of errors and progress
    entries_changed = 0
    errors = 0

    while name:
        try:
            name_regex = re.compile(name, re.IGNORECASE)
            cell = sheet.find(name_regex)

            # print("Found something at R%s C%s" % (cell.row, cell.col))
            # print("Updating values B%s\n" % (cell.row))
            # ex.) B1 -> (Column + Row)

            sheet.update_cell(cell.row, config.CELL_COL, config.CELL_CONTENT) # Update the value of the current cell

            entries_changed += 1

            name = fpr.readline().strip() # Continue iterating through file
        except:
            # print("FAILED TO COMPUTE FOR: %s\n" % (name)) # Error Message for feedback
            fp_err.write("FAILED TO COMPUTE FOR: %s\n" % (name)) # Error Message for feedback to error.txt
            errors += 1
            name = fpr.readline().strip() # Continue iterating through file
            continue # Skip back to beginning of loop

    # Updating entries_changed label    
    if (entries_changed == 1):
        entries_changed_counter.set("%s cell has been updated." % (entries_changed))
    else:
        entries_changed_counter.set("%s cells have been updated." % (entries_changed))
    
    # Updating errors_occurred label
    if (errors == 0):
        errors_occured_counter.set("%s errors have occured." % (errors))
    elif (errors == 1):
        errors_occured_counter.set("%s error has occured.\nCheck the error.txt file for more information." % (errors))
    else:
        errors_occured_counter.set("%s errors have occured.\nCheck the error.txt file for more information." % (errors))

    # Updating progress_message label
    if entries_changed > 0:
        progress_message.set("Success!")
        if errors > 0:
            progress_message.set("Successfully inputted some cells, check error log.")
    elif entries_changed == 0:
        progress_message.set("None of the cells changed, check error.txt!")

    # Close file i/o
    fpr.close()
    fp_err.close()