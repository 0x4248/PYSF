# Python Script Framework 
from urllib import parse

##############################################
import sys
sys.path.append("....")
from __main__ import verbose as PYSF_VERBOSE
##############################################

def run(ARGS):
    ##############################################
    #DEFAULTS
    URL = ""
    #GETTING ARGS FROM PYSF
    for i in ARGS:
        if i.startswith("URL"):
            URL = i.split(":$:$:")[1]
    #CHECKING REQUIRED               
    if URL == "":
        return "MISSINGARG:URL"   
    #FORMAT
    try:
        URL = str(URL)
    except TypeError:
        return "TYPE_ERR"
    ##############################################    
    URL = URL.strip()
    if not parse.urlparse(URL).scheme:
        URL = 'http://' + URL
    return URL

if __name__ == "__main__":
    print("This script needs to be run in PYS")