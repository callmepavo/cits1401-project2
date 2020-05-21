# CITS1401  Project 2
# Zach Manson 22903345
# 2020-05-14
'''
TODO
 - Comments
 - Edge cases
 - Reread project spec
 - Find out how to handle reading 0 as a numbers first digit
'''


def main(filename, no_places, regularise=False):
    lines = processFile(filename)
    if lines == None:
         return([])
    
    all_numbers = getNumbers(lines)
    
    digit_lists = [getDigitCount(all_numbers, i) for i in range(no_places)]
    
    if regularise:
        return(getRegularisedLists(digit_lists))
        
    return(digit_lists)

# Returns list of strings, each a line of the file filename
def processFile(filename):
    try: # Error checking: doesn't crash if can't find file
        file = open(filename,"r")
    except FileNotFoundError:
        print("Error: File not found!  Exiting gracefully.")
        return(None)
    
    lines = [line for line in file]
    file.close()
    
    return(lines)


# Returns all the valid numbers from the file
# Extracts from lines and sanitises them
def getNumbers(lines):
    numbers = []
    lines_sans_header = lines[1:]
    for record in lines_sans_header:
        # remove \n, split on comma, remove first item (name)
        record_as_list = record.replace("\n", "").split(",")[1:]
        # remove blank from end if there is one
        if len(record_as_list) > 0 and record_as_list[-1] == '':
            del record_as_list[-1] 
        
        for number in record_as_list:
            try: # if its not a number, skip it
                float(number)
            except ValueError:
                continue
            
            if number[0] == "-": # remove negative sign
                number = number[1:]
            if "." in number: # remove everything after decimal point
                number = number[:number.index(".")]
            
            numbers.append(number) # append sanitised string number to numbers
    
    return(numbers)


# Returns list of counts for each digit in position from list of all numbers
def getDigitCount(all_numbers, position):
    digits = [0 for i in range(10)]
    for number in all_numbers:
        try: # if there isn't a digit at position, ignore error
            digits[int(number[position])] += 1
        except IndexError:
            pass
    
    digits = digits[1:] + [digits[0]] # rotate so 0 count is last position
    
    return(digits)


def getRegularisedLists(digit_lists):
    # fill reg_lists with correct num of empty lists
    reg_lists = [[] for i in range(len(digit_lists))] 
    
    for i in range(len(digit_lists)):
        total = sum( digit_lists[i] )
        for j in range(len( digit_lists[i] )):
            reg_lists[i].append( round(digit_lists[i][j] / total, 4) )
    
    return(reg_lists)