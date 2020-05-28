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
    # Validate inputs
    if not (isinstance(filename, str)
            and isinstance(no_places, int)
            and (isinstance(regularise, bool) 
                 or regularise == 0
                 or regularise == 1)    ):
        print("Error: Input type wrong.  Exiting gracefully.")
        return([])
    
    if no_places < 1:
        print("Error: Num places not positive.  Exiting gracefully.")
        return([])
    # Get lines from file
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
    for record in lines:
        # remove \n, split on comma
        record_as_list = record.replace("\n", "").split(",")
        
        for number in record_as_list:
            # skip if contains letters, do this since 4e5 is valid float()
            # input but invalid for this program
            if number.isupper() or number.islower():
                continue
            try: # if its not a number, skip it
                # float() removes formats .45 to 0.45 and changes 05 to 5.0
                # int() turns 0.45 to 0 or 5.0 to 5
                # abs() makes number positive -5 to 5
                # str() converts now sanitised num to string
                number = str(abs(int(float((number)))))
            except ValueError: # if error occurs its not a valid number, skip it
                continue
            
            numbers.append(number) # append sanitised string number to numbers
    
    return(numbers)

# Returns list of counts for each digit in position from list of all numbers
def getDigitCount(all_numbers, position):
    digits = [0 for i in range(10)] # Create a list with inital values
    for number in all_numbers:
        try: # if there isn't a digit at position, ignore error
            digits[int(number[position])] += 1
        except IndexError:
            pass
    
    digits = digits[1:] + [digits[0]] # rotate so 0 count is last position
    
    return(digits)

# Returns input lists as rounded fractions
def getRegularisedLists(digit_lists):
    # fill reg_lists with correct num of empty lists
    reg_lists = [[] for i in range(len(digit_lists))] 
    
    for i in range(len(digit_lists)):
        total = sum( digit_lists[i] )
        if total == 0: continue # Skip if there are no digits
        for j in range(len( digit_lists[i] )):
            reg_lists[i].append( round(digit_lists[i][j] / total, 4) )
    
    return(reg_lists)