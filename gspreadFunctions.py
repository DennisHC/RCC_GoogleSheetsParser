# Global Variables
from config import CELL_COL, CELL_CONTENT, GOOGLE_SHEETS_FILENAME

def retrieve_spreadsheet_name(self, *args):
    config.GOOGLE_SHEETS_FILENAME = spreadsheet_name.get()

# New implementation: Inputting Letters
def retrieve_cell_col(self, *args):
    temp = cell_col.get()
    temp = temp.upper()
    result = 0

    for i, T, in enumerate(temp[::-1]):
        letter_number = ord(T) - ord("A") + 1
        result += letter_number * (26 ** i)
    config.CELL_COL = result

def retrieve_cell_content(self, *args):
    config.CELL_CONTENT = cell_content.get()