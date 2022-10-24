# Python Script Framework 
import requests

##############################################
import sys
sys.path.append("....")
from __main__ import verbose as PYSF_VERBOSE
##############################################

def run(ARGS):
    ##############################################
    #DEFAULTS
    URL = ""
    FILE = ""
    #GETTING ARGS FROM PYSF
    for i in ARGS:
        if i.startswith("URL"):
            URL = i.split(":$:$:")[1]
        if i.startswith("FILE"):
            FILE = i.split(":$:$:")[1]
    #CHECKING REQUIRED               
    if URL == "":
        return "MISSINGARG:URL"   
    #FORMAT
    try:
        URL = str(URL)
        FILE = str(FILE)
    except TypeError:
        return "TYPE_ERR"
    ##############################################    
    if URL.upper().startswith("HTTP://") == False and URL.upper().startswith("HTTPS://") == False:
        PYSF_VERBOSE.question("Does this use http or https")
        while True:
            ask = input("[HTTP/HTTPS]>")
            if ask.upper().startswith("HTTP"):
                URL = "http://"+URL
                break
            if ask.upper().startswith("HTTPS"):
                URL = "https://"+URL
                break
    PYSF_VERBOSE.info("Attempting to contact "+URL)
    
    try:
        r = requests.get(URL)
    except Exception as e:
        PYSF_VERBOSE.critical(e)
        return 1
    if r.status_code == 200:
        PYSF_VERBOSE.log("HTTP 200")
    else:
        PYSF_VERBOSE.warn("HTTP "+str(r.status_code))
    PYSF_VERBOSE.log("Downloaded content")
    if FILE != "":
        open(FILE, "w").write(r.text)
    print(r.text)
    return 0
if __name__ == "__main__":
    print("This script needs to be run in PYS")