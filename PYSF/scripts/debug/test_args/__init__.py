import sys

sys.path.append("....")
from __main__ import verbose as PYSF_VERBOSE


def run(ARGS):
    ################################
    # DEFAULTS
    _1 = 1
    _2 = "Hello"
    _3 = True
    _4 = ""
    # GETTING ARGS FROM PYSF
    for i in ARGS:
        if i.startswith("_1"):
            _1 = i.split(":$:$:")[1]
        if i.startswith("_2"):
            _2 = i.split(":$:$:")[1]
        if i.startswith("_3"):
            _3 = i.split(":$:$:")[1]
        if i.startswith("_4"):
            _4 = i.split(":$:$:")[1]
    # CHECKING REQUIRED
    if _4 == "":
        return "MISSINGARG:_4"
    # FORMAT
    try:
        _1 = int(_1)
        _2 = str(_2)
        _3 = bool(_3)
        _4 = str(_4)
    except TypeError:
        return "TYPE_ERR"
    ################################
    PYSF_VERBOSE.warn("Test")
    print(_1, _2, _3, _4)
    return 0


if __name__ == "__main__":
    print("This script needs to be run in PYS")
