# Python Script Framework
# Put below here modules you wish to import
import base64

##############################################
import sys

sys.path.append("....")
from __main__ import verbose as PYSF_VERBOSE

##############################################


def run(ARGS):
    ##############################################
    # DEFAULTS
    INPUT = ""
    # GETTING ARGS FROM PYSF
    for i in ARGS:
        if i.startswith("INPUT"):
            INPUT = i.split(":$:$:")[1]
    # CHECKING REQUIRED
    if INPUT == "":
        return "MISSINGARG:INPUT"
    # FORMAT
    try:
        INPUT = str(INPUT)
    except TypeError:
        return "TYPE_ERR"
    ##############################################
    PYSF_VERBOSE.log("Converting")
    return base64.b64encode(INPUT.encode()).decode("utf-8")


if __name__ == "__main__":
    print("This script needs to be run in PYS")
