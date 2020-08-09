def retrieveInputForTextFile():
    inputValue = textBox.get("1.0", "end-1c")
    fp.write(inputValue)
    print(inputValue)

############ DEBUGING ##############

def retrieveInputForGlobalVars():
    someValue = spreadSheetTextBox.get("1.0", "end-1c")
    print(someValue)
    print("This button has been pressed!")
    global GOOGLE_SHEETS_FILENAME
    GOOGLE_SHEETS_FILENAME = someValue
    print(GOOGLE_SHEETS_FILENAME)

############ DEBUGING ##############

#def globalValueTest(globalVar):
##    print(type(finalButton))
#    fp.write(globalVar)