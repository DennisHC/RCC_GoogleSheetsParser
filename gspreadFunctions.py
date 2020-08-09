def makeChangesToSpreadsheet():
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

    print("input.txt file parsing completed")