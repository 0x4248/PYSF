# Python Script Framework 
#Put below here modules you wish to import
import ipaddress
from subprocess import Popen, PIPE

##############################################
import sys
sys.path.append("....")
from __main__ import verbose as PYSF_VERBOSE
##############################################

def run(ARGS): 
        PYSF_VERBOSE.warn("This process will take time")
        net4 = ipaddress.ip_network('192.168.1.0/24')
        for x in net4.hosts():
                x = str(x)
                hostup = Popen(["ping","-n","1","-w","1",x], stdout=PIPE)
                output = hostup.communicate()[0]
                val1 = hostup.returncode
                if val1 == 0:
                        PYSF_VERBOSE.plus(x+ " is pinging")
                else:
                        PYSF_VERBOSE.minus(x+ " is not responding")
if __name__ == "__main__":
    print("This script needs to be run in PYS")