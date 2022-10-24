import random 

def run(ARGS):
    ################################
    #DEFAULTS
    AMOUNT = ""
    RANDOM = False
    #GETTING ARGS FROM PYSF
    for i in ARGS:
        if i.startswith("AMOUNT"):
            AMOUNT = i.split(":$:$:")[1]
        if i.startswith("RANDOM"):
            AMOUNT = i.split(":$:$:")[1] 
    #CHECKING REQUIRED               
    if AMOUNT == "":
        return "MISSINGARG:AMOUNT"   
    #FORMAT
    try:
        AMOUNT = int(AMOUNT)
        RANDOM = bool(RANDOM)
    except TypeError:
        return "TYPE_ERR"
    ################################    
    if AMOUNT == "":
        return 0
    for i in range(AMOUNT):
        if RANDOM:
            print(i + random.randint(1,10))
        else:
            print(i)

if __name__ == "__main__":
    print("This script needs to be run in PYS")