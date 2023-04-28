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
    byte_array = bytearray(INPUT, "utf8")

    byte_list = []

    for byte in byte_array:
        binary_representation = bin(byte)
        byte_list.append(binary_representation)

    print(" ".join(str(e) for e in byte_list).replace("b", ""))
    return 0


if __name__ == "__main__":
    print("This script needs to be run in PYS")
