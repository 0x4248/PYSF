# Python Script Framework 
import socket 
import threading


##############################################
import sys
sys.path.append("....")
from __main__ import verbose as PYSF_VERBOSE
##############################################

def port_scanner(target,port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        PYSF_VERBOSE.log(f"Port {port} is open")
    except Exception as e:
        pass

def run(ARGS):
    ##############################################
    #DEFAULTS
    TARGET = ""
    #GETTING ARGS FROM PYSF
    for i in ARGS:
        if i.startswith("TARGET"):
            TARGET = i.split(":$:$:")[1]
    #CHECKING REQUIRED               
    if TARGET == "":
        return "MISSINGARG:TARGET"   
    #FORMAT
    try:
        TARGET = str(TARGET)
    except TypeError:
        return "TYPE_ERR"
    ##############################################    
    for port in range(1,5050):
        thread = threading.Thread(target =port_scanner, args=[TARGET,port])
        thread.start()
    return 0
if __name__ == "__main__":
    print("This script needs to be run in PYS")