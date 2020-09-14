import gspread
from oauth2client.service_account import ServiceAccountCredentials
from tkinter import *
from tkinter import ttk

CELL_COL = "D"
CELL_CONTENT = "1"
GOOGLE_SHEETS_FILENAME = "Copy of 20-21 Points Sheet Template (Color Change)"
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open(GOOGLE_SHEETS_FILENAME).sheet1
