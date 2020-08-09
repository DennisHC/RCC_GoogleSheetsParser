# Problems with Development so far:
#   1) Name has to be exact spelling (this one would be difficult to fix because I would need machine learning)
#   2) Name has to have exact same format (ex. Name cannot be all lowercase or uppercase)
#   3) Try and catch does not exist for opening file
#   4) Provide an error message if the text file is empty

# Future Iterations:
#   1) Create a friendly GUI and/or a BATCH File (Kivy)
#   2) Figure out how to request custom columns (for events)
#   3) Create an output file for errors

# SOLVED:
#   1) **FIXED** Try and catch needs to be implemented, and loop needs to continue going if name is not found
#       a) **FIXED** Program crashes when name is end of list (Fix using continue?)

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

# Global Variables
CELL_COL = 2
CELL_CONTENT = "8"
GOOGLE_SHEETS_FILENAME = "Google Sheets Parser Test"

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open(GOOGLE_SHEETS_FILENAME).sheet1

# Extract and print all of the values
# list_of_hashes = sheet.get_all_records()
# print(list_of_hashes)

# Working with files
try:
    fp = open("input.txt")
except:
    print("File to open does not exist")
    # exit()
name = fp.readline().strip()
while name:
    try:
        cell = sheet.find(name)
        print(name)
        print("Found something at R%s C%s" % (cell.row, cell.col))
        print("Updating values B%s\n" % (cell.row))

        sheet.update_cell(cell.row, CELL_COL, CELL_CONTENT) # Arg 2, 3 should be custom if possible

        name = fp.readline().strip() # Continue iterating through file
    except:
        print("FAILED TO COMPUTE FOR %s\n" % (name)) # Error Message for feedback to user (possibly put this into an output log)
        name = fp.readline().strip() # Continue iterating through file
        continue # Skip back to beginning of loop

print("Dennis' Google Sheets Parser has finished running successfully.")
fp.close()