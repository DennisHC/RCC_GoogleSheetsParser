# Clear/erase a file
def clear_file(file_name):
    fp = open(file_name, "w+")
    fp.seek(0)
    fp.truncate()
    fp.close()