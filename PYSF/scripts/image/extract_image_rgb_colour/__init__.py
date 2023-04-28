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
    FILE = ""
    # GETTING ARGS FROM PYSF
    for i in ARGS:
        if i.startswith("FILE"):
            FILE = i.split(":$:$:")[1]
    # CHECKING REQUIRED
    if FILE == "":
        return "MISSINGARG:FILE"
    # FORMAT
    try:
        FILE = str(FILE)
    except TypeError:
        return "TYPE_ERR"
    ##############################################
    try:
        from PIL import Image
    except:
        PYSF_VERBOSE.error(
            "Pillow is not installed on your python installation install pillow using pip. Please run pip install pillow"
        )
        return 1
    img = Image.open(FILE)
    PYSF_VERBOSE.log("Opened image " + FILE)
    data = img.getdata()
    r = [(d[0], 0, 0) for d in data]
    g = [(0, d[1], 0) for d in data]
    b = [(0, 0, d[2]) for d in data]
    img.putdata(r)
    img.save("/".join(FILE.split("/")[:-1]) + "/red-" + FILE.split("/")[-1])
    img.putdata(g)
    img.save("/".join(FILE.split("/")[:-1]) + "/green-" + FILE.split("/")[-1])
    img.putdata(b)
    img.save("/".join(FILE.split("/")[:-1]) + "/blue-" + FILE.split("/")[-1])
    return 0


if __name__ == "__main__":
    print("This script needs to be run in PYS")
