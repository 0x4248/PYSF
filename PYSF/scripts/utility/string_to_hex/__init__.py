# Python Script Framework
# Put below here modules you wish to import

##############################################
import sys

sys.path.append("....")
from __main__ import verbose as PYSF_VERBOSE

##############################################


def run(ARGS):
    ##############################################
    # DEFAULTS
    INPUT = ""
    SPLIT = 0
    # GETTING ARGS FROM PYSF
    for i in ARGS:
        if i.startswith("INPUT"):
            INPUT = i.split(":$:$:")[1]
        if i.startswith("SPLIT"):
            SPLIT = i.split(":$:$:")[1]
    # CHECKING REQUIRED
    if INPUT == "":
        return "MISSINGARG:INPUT"
    # FORMAT
    try:
        INPUT = str(INPUT)
        SPLIT = int(SPLIT)
    except TypeError:
        return "TYPE_ERR"
    ##############################################
    PYSF_VERBOSE.log("Converting")
    INPUT = INPUT.encode().hex()
    if SPLIT != 0:
        for i in range(SPLIT):
            print("=", end="")
        print("")
        INPUT = "\n".join(INPUT[i : i + SPLIT] for i in range(0, len(INPUT), SPLIT))
        print(INPUT)
        for i in range(SPLIT):
            print("=", end="")
        print("")
    else:
        print(INPUT)
    return 0


if __name__ == "__main__":
    print("This script needs to be run in PYS")
