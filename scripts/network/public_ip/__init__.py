# Python Script Framework 
import requests

##############################################
import sys
sys.path.append("....")
from __main__ import verbose as PYSF_VERBOSE
##############################################

def run(ARGS):
    PYSF_VERBOSE.info("Attempting to contact ifconfig.co")
    try:
        response = requests.get('https://api.ipify.org')
    except Exception as e:
        PYSF_VERBOSE.critical("Failed to contact ifconfig.co")
        PYSF_VERBOSE.critical(e)
    return str(response.text)
if __name__ == "__main__":
    print("This script needs to be run in PYS")