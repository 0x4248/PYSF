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
    ARG = "Hello World"
    # GETTING ARGS FROM PYSF
    for i in ARGS:
        if i.startswith("ARG"):
            ARG = i.split(":$:$:")[1]
    # CHECKING REQUIRED
    # if ARG == "":
    #    return "MISSINGARG:ARG"
    # FORMAT
    try:
        ARG = str(ARG)
    except TypeError:
        return "TYPE_ERR"
    ##############################################
    # Write your script here


if __name__ == "__main__":
    print("This script needs to be run in PYS")
