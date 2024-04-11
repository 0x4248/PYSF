# PYSF Python Script Foundation
# GNU v3
# Owner: awesomelewis2007
# Github: https://www.github.com/0x4248/PYSF
# If you need help on knowing how PYSF works head over to https://www.github.com/0x4248/PYSF and read the readme.md

import os
import random
import sys
import platform
import json
import threading
import time
import traceback
from colorama import Fore, Back, Style
import importlib

# This is used in the create function
DEFAULT_SCRIPT = """# Python Script Framework (V1)
#Put below here modules you wish to import


##############################################
import sys
sys.path.append("....")
from __main__ import verbose as PYSF_VERBOSE
##############################################

def run(ARGS):
    ##############################################
    #DEFAULTS
    ARG = "Hello World"
    #GETTING ARGS FROM PYSF
    for i in ARGS:
        if i.startswith("ARG"):
            ARG = i.split(":$:$:")[1]
    #CHECKING REQUIRED               
    #if ARG == "":
    #    return "MISSINGARG:ARG"   
    #FORMAT
    try:
        ARG = str(ARG)
    except TypeError:
        return "TYPE_ERR"
    ##############################################    
    #Write your script here

if __name__ == "__main__":
    print("This script needs to be run in PYS")"""

VERSION = "0.1.1 ALPHA"


class verbose:
    def log(message):
        print(Fore.GREEN + "[+] " + Style.RESET_ALL + message)

    def question(message):
        print(Fore.YELLOW + "[?] " + Style.RESET_ALL + message)

    def warn(message):
        print(Fore.YELLOW + "[!] " + Style.RESET_ALL + message)

    def error(message):
        print(Fore.RED + "[-] " + Style.RESET_ALL + message)

    def critical(message):
        print(Fore.RED + "[x] " + Style.RESET_ALL + message)

    def info(message):
        print(Fore.CYAN + "[*] " + Style.RESET_ALL + message)


if __name__ == "__main__":
    print("Starting PYSF...", end="\r")
    # This is to get the path correct
    path = os.path.dirname(__file__)
    sys.path.append(path)
    os.chdir(path)

    time.sleep(0.2)
    sys.stdout.write("\033[K")
    print(
        Fore.CYAN
        + r"""
 ________  ___    ___ ________  ________ 
|\   __  \|\  \  /  /|\   ____\|\  _____\
\ \  \|\  \ \  \/  / | \  \___|\ \  \__/ 
 \ \   ____\ \    / / \ \_____  \ \   __\
  \ \  \___|\/  /  /   \|____|\  \ \  \_|
   \ \__\ __/  / /       ____\_\  \ \__\ 
    \|__||\___/ /       |\_________\|__| 
         \|___|/        \|_________|     """
        + Style.RESET_ALL
    )
    print("============================================")
    print("Welcome to the Python Script Framework")
    print("If you need help type help to get started")
    verbose.info(str("Running on: " + platform.system() + " " + platform.version()))
    verbose.info("Version: " + VERSION)
    script = ""
    args = []
    num = 0
    last_search = []
    if platform.system() == "Linux":
        for i in os.walk("scripts/"):
            if i[0].endswith("__pycache__"):
                continue
            if i[0].count("/") == 2:
                num = num + 1
    else:
        for i in os.walk("scripts\\"):
            if i[0].endswith("__pycache__"):
                continue
            if i[0].count("\\") == 2:
                num = num + 1
    print("There are" + Fore.GREEN, num, Style.RESET_ALL + "scripts installed")
    print("============================================")
    time.sleep(0.2)
    while True:
        try:
            if script == "":
                cmdline = input("PYSF>")

            else:
                cmdline = input(
                    "PYSF Script(" + Fore.CYAN + script + Style.RESET_ALL + ")>"
                )

            if cmdline.startswith("$"):
                os.system(cmdline[1:])

            if cmdline.startswith("use"):
                if os.path.isdir(cmdline[4:]):
                    pass
                else:
                    if cmdline[4:].isdigit():
                        try:
                            index = int(cmdline[4:])
                            script = last_search[index]
                            if os.path.isfile(script + "/PYSFSCRIPT"):
                                verbose.log("Set script to " + script)
                            else:
                                verbose.error("DIR exists but no PYSFSCRIPT file found")
                                verbose.info(
                                    "Add a PYSFSCRIPT file to make PYSF see the script"
                                )
                            continue
                        except IndexError:
                            verbose.error("Script number was not in last list/search")
                            continue
                    else:
                        verbose.error("DIR does not exist")
                        continue
                if os.path.isfile(cmdline[4:] + "/PYSFSCRIPT"):
                    verbose.log("Set script to " + cmdline[4:])
                else:
                    verbose.error("DIR exists but no PYSFSCRIPT file found")
                    verbose.info("Add a PYSFSCRIPT file to make PYSF see the script")
                    continue
                script = cmdline[4:]

            if cmdline.startswith("info"):
                if script == "":
                    verbose.error("No script set")
                    continue
                else:
                    with open(script + "/info.json", "r") as infofile:
                        infojson = json.load(infofile)
                    print("Name: " + infojson["name"])
                    print("Description: " + infojson["description"])
                    try:
                        print("Requires: " + str(infojson["packages"]))
                    except:
                        print("No requirements found")
                    print("\nARG\t\t|REQUIRED\t|DEFAULT")
                    for i in range(len(infojson["args"])):
                        print(
                            str(infojson["args"][i])
                            + "\t\t|"
                            + str(infojson["required"][i])
                            + "\t\t|"
                            + str(infojson["defaults"][i])
                        )

            if cmdline.startswith("set"):
                cmd = cmdline.split(" ")
                ignore = False
                for i in args:
                    if i.startswith(cmd[1]):
                        ignore = True
                        verbose.question(str("Overwrite variable " + cmd[1]))
                        confirm = input("[Y/n]")
                        if confirm.upper() == "Y":
                            del args[args.index(i)]
                            args.append(cmd[1] + ":$:$:" + " ".join(cmd[2:]))
                            print(cmd[1] + "->" + " ".join(cmd[2:]))

                            break
                        else:
                            verbose.error("Canceled overwrite")
                            break

                if ignore == False:
                    args.append(cmd[1] + ":$:$:" + " ".join(cmd[2:]))
                    print(cmd[1] + "->" + " ".join(cmd[2:]))
                del cmd, ignore

            if cmdline == "listargs":
                print("NAME\t\tDATA")
                print("--------------------------")
                for i in args:
                    print(i.replace(":$:$:", "\t\t"))

            if cmdline == "clearargs":
                verbose.question("Are you sure?")
                confirm = input("[Y/n]")
                if confirm.upper() == "Y":
                    args = ""
                    verbose.log("Cleared args")
                else:
                    verbose.info("Canceled operation")
            if cmdline == "run" or cmdline == "execute":
                if script == "":
                    verbose.error("No script is set")
                    continue
                try:
                    script_module = importlib.import_module(
                        script.replace("/", ".").replace("\\", ".")
                    )
                    importlib.reload(script_module)
                    script_return = script_module.run(args)
                    if script_return == None:
                        verbose.info("Script ended with out any exit message/code")
                    elif script_return == 0:
                        verbose.log("Script ended successfully (Code 0)")
                    elif script_return == 1:
                        verbose.error("Script ended unsuccessfully (Code 1)")
                    elif script_return.startswith("MISSINGARG"):
                        verbose.critical(
                            str(
                                "The var "
                                + Fore.RED
                                + script_return.split(":")[1]
                                + Style.RESET_ALL
                                + " is not set"
                            )
                        )
                    else:
                        verbose.info(script_return)
                    del script_module, script_return
                except Exception as e:
                    print(
                        "========= "
                        + Fore.RED
                        + "[X]"
                        + Style.RESET_ALL
                        + " PYSF Traceback "
                        + Fore.RED
                        + "[X]"
                        + Style.RESET_ALL
                        + " ========="
                    )
                    print(sys.exc_info())
                    print("==========================================")
                    print(traceback.format_exc())
                    print("==========================================")
                    verbose.critical(str(e))

            if cmdline == "list":
                last_search = []
                num = 0
                for i in os.walk("scripts\\"):
                    if i[0].endswith("__pycache__"):
                        continue
                    if i[0].count("\\") == 2:
                        print(num, i[0])
                        last_search.append(i[0])
                        num = num + 1
                if random.randint(1, 3) == 1:
                    print(
                        Fore.YELLOW
                        + "[TIP]"
                        + Style.RESET_ALL
                        + " You can run use <number> to use a script from the numbered list"
                    )

            if cmdline.startswith("search"):
                last_search = []
                num = 0
                cmd = cmdline.split(" ")
                for i in os.walk("scripts\\"):
                    if i[0].endswith("__pycache__"):
                        continue
                    if i[0].count("\\") == 2:
                        term = " ".join(cmd[1:])
                        if (
                            i[0]
                            .replace("scripts\\", "")
                            .replace("scripts/", "")
                            .find(term)
                            != -1
                        ):
                            with open(i[0] + "/info.json", "r") as infofile:
                                infojson = json.load(infofile)
                            out = i[0]
                            print(
                                Fore.CYAN
                                + str(num)
                                + Style.RESET_ALL
                                + "\t"
                                + out
                                + "\t\t"
                                + infojson["name"]
                            )
                            last_search.append(i[0])
                            num = num + 1
                if random.randint(1, 3) == 1:
                    print(
                        Fore.YELLOW
                        + "[TIP]"
                        + Style.RESET_ALL
                        + " You can run use <number> to use a script from the numbered list"
                    )

            if cmdline == "create":
                name = input("Name of script (e.g test script)>")
                fname = input("folder name (e.g test_script)>")
                description = input("Description of script>")
                print(
                    "Enter name of first argument leave blank to not create any arguments"
                )
                script_args = []
                defaults = []
                require = []
                while True:
                    arg_input = input("Name>").upper()
                    if arg_input == "":
                        break
                    defaults_input = input("Default data (Leave blank for none)>")
                    if defaults_input == "":
                        require_input = True
                    else:
                        require_input = input("Is this arg required [Y/n]>")
                        if require_input == "Y":
                            require_input = True
                        else:
                            require_input = False
                    script_args.append(arg_input)
                    defaults.append(defaults_input)
                    require.append(require_input)
                    print("Saved! Enter next argument name or leave blank to stop")
                    script = {}
                    script["name"] = name
                    script["description"] = description
                    script["args"] = script_args
                    script["defaults"] = defaults
                    script["required"] = require
                os.mkdir("./scripts/user/" + fname)
                with open("./scripts/user/" + fname + "/info.json", "w") as jsonfile:
                    json.dump(script, jsonfile)
                script = "scripts/user/" + fname
                open("./scripts/user/" + fname + "/PYSFSCRIPT", "w").write(
                    "This file is fo that PYSF can find this script. Don't remove it"
                )
                open("./scripts/user/" + fname + "/__init__.py", "w").write(
                    DEFAULT_SCRIPT
                )

            if cmdline == "help":
                print(open("./help", "r").read())

            if cmdline == "version":
                print(VERSION)

            if (
                cmdline.startswith("exit")
                or cmdline.startswith("quit")
                or cmdline == "e"
                or cmdline == "q"
            ):
                exit()
        except KeyboardInterrupt:
            print("")
            verbose.warn("To exit type exit or quit")
