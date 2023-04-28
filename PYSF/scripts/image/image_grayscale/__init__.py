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
    OUTPUT_FILE = ""
    # GETTING ARGS FROM PYSF
    for i in ARGS:
        if i.startswith("FILE"):
            FILE = i.split(":$:$:")[1]
        if i.startswith("OUTPUT_FILE"):
            OUTPUT_FILE = i.split(":$:$:")[1]
    # CHECKING REQUIRED
    if FILE == "":
        return "MISSINGARG:FILE"
    if OUTPUT_FILE == "":
        return "MISSINGARG:FILE"
    # FORMAT
    try:
        FILE = str(FILE)
        OUTPUT_FILE = str(OUTPUT_FILE)
    except TypeError:
        return "TYPE_ERR"
    ##############################################
    try:
        from PIL import Image, ImageEnhance
    except:
        PYSF_VERBOSE.error(
            "Pillow is not installed on your python installation install pillow using pip. Please run pip install pillow"
        )
        return 1
    img = Image.open(FILE)
    PYSF_VERBOSE.log("Opened image " + FILE)
    converter = ImageEnhance.Color(img)
    img2 = converter.enhance(0)
    img2.save(OUTPUT_FILE)
    return 0


if __name__ == "__main__":
    print("This script needs to be run in PYS")
