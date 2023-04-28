# Python Script Framework
import socket


##############################################
import sys

sys.path.append("....")
from __main__ import verbose as PYSF_VERBOSE

##############################################


def run(ARGS):
    return socket.gethostbyname(
        socket.gethostname()
    )  # local IP adress of your computer


if __name__ == "__main__":
    print("This script needs to be run in PYS")
