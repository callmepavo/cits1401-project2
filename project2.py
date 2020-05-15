# CITS1401  Project 2
# Zach Manson 22903345
# 2020-05-14

def main(filename, no_places, regularise=False):
    lines = processFile(filename)
    if lines == None:
        return([])
    all_numbers = getNumbers(lines)
    
    
def processFile(filename):
    # Error checking: doesn't crash if filename doesn't exist
    try:
        file = open(filename,"r")
    except FileNotFoundError:
        print("Error: File doesn't exist!  Exiting gracefully.")
        return(None)
    
    lines = []
    for line in file:
        lines.append(line)        
    
    file.close()
    
    return(lines)

def getNumbers(lines):
    #data_lines = lines[1:]
    numbers = []
    lines_sans_header = lines[1:]
    for record in lines_sans_header:
        record_as_list = record.replace("\n", "").split(",")
        record_as_list = record_as_list[1:] # remove name
        
        if len(record_as_list) > 0 and record_as_list[-1] == '': #remove blank from end if there is one
            del record_as_list[-1] 
        
        for i in record_as_list:
            num = float(i)
            numbers.append(num)
    print(numbers)
    
    
    return()


output = main("sample_accounts.csv", 1)
print(output)