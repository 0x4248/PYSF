# Python Script Framework 
import random

##############################################
import sys
sys.path.append("....")
from __main__ import verbose as PYSF_VERBOSE
##############################################

def run(ARGS):
    ##############################################
    #DEFAULTS
    SIZE = 8
    AMOUNT = 10
    FILE = ""
    SHOW_NUM = True
    #GETTING ARGS FROM PYSF
    for i in ARGS:
        if i.startswith("SIZE"):
            SIZE = i.split(":")[1]
        if i.startswith("AMOUNT"):
            AMOUNT = i.split(":")[1]
        if i.startswith("FILE"):
            FILE = i.split(":")[1]    
        if i.startswith("SHOW_NUM"):
            SHOW_NUM = i.split(":")[1]    
    #FORMAT
    try:
        SIZE = int(SIZE)
        AMOUNT = int(AMOUNT)
        FILE = str(FILE)
        SHOW_NUM = bool(SHOW_NUM)
    except TypeError:
        return "TYPE_ERR"
    ##############################################
    chars = ["A","B","C","D","E","F"]
    PYSF_VERBOSE.plus("Generating hex numbers")    
    if FILE != "":
         PYSF_VERBOSE.plus("Will write number to "+FILE)  
    for i in range(AMOUNT):
        number = ""
        for i in range(SIZE):
            if random.randint(1,2) == 1:
               number = number + str(random.randint(0,9))
            else:
                number = number + random.choice(chars)
        if SHOW_NUM == True:
            print(number)
        if FILE != "":
            try:
                open(FILE,"w").write(number)
            except:
                PYSF_VERBOSE.minus("Can't write to the file "+FILE)
    return 0
if __name__ == "__main__":
    print("This script needs to be run in PYS")