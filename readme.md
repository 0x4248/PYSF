# PYSF

A project similar to Metasploit but made in python and not just exploits.

PYSF means Python Script Framework

# How to use PYSF

Download the reposity and change dirs to where `__main__.py` is then run python __main__.py it should start up PYSF.

It should look like this
```

 ________  ___    ___ ________  ________
|\   __  \|\  \  /  /|\   ____\|\  _____\
\ \  \|\  \ \  \/  / | \  \___|\ \  \__/
 \ \   ____\ \    / / \ \_____  \ \   __\
  \ \  \___|\/  /  /   \|____|\  \ \  \_|
   \ \__\ __/  / /       ____\_\  \ \__\
    \|__||\___/ /       |\_________\|__|
         \|___|/        \|_________|
============================================
Welcome to the Python Script Framework
[*] Running on: Windows 10.0.19044
[*] Version: 0.1 ALPHA
THere are 10 scripts installed
============================================
```

# How to run a script

To run a script you need to select it lets use the number generator script.

To start we can search the script by using `search number`

```
PYSF>search number
scripts\debug\number    
scripts\generator\number
PYSF>
```

Then we select the script.

```
PYSF>use scripts\generator\number
[+] Set script to scripts\generator\number
PYSF Script(scripts\generator\number)> 

```

The script is selected and it shows on the command input.

We can get info about the script using `info`

```
PYSF Script(scripts\generator\number)>info
Generates Numbers
This script generates numbers and prints them to the screen use FILE 
argument to output numbers to a file.
No requirements
ARG             |REQUIRED       |DEFAULT
SIZE            |True           |8
AMOUNT          |False          |10
FILE            |False          |
SHOW_NUM        |True           |True
PYSF Script(scripts\generator\number)>
```

We can change arguments using `set` 

```
PYSF Script(scripts\generator\number)>set SIZE 5 
SIZE->5
PYSF Script(scripts\generator\number)>
```

We can run the script using `run` or `execute`

```
PYSF Script(scripts\generator\number)>run
[+] Generating numbers
89640
47385
13883
66747
60171
98030
06483
66020
67208
45968
[+] Script ended successfully (Code 0)
PYSF Script(scripts\generator\number)>
```

If a required argument is missing then it will return an error

```
PYSF Script(scripts\utility\base32_to_string)>run
[x] The var INPUT is not set
PYSF Script(scripts\utility\base32_to_string)>
```

Be sure to keep your scripts up to date by reinstalling PYSF

