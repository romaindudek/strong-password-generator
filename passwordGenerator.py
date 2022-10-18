#!/usr/bin/env python3

import random
import math
import string
import sys

ASCII_SET = string.ascii_uppercase + string.ascii_lowercase
DIGITS = string.digits
SPEC_CHAR_SET = ''.join([char for char in string.punctuation if char not in "\\\"'^`.,:?"])

def pickupChar(charSet):
    return random.choice(charSet)

def generatePass(includeSpecials:bool = True, defaultLength: int = 12, showStats: bool=False):
    output=""
    if not includeSpecials:
        for i in range(0, defaultLength -2):
            output += pickupChar(ASCII_SET)
        output += pickupChar(DIGITS) + pickupChar(DIGITS)
    else:
        for i in range(0, defaultLength - 3):
            output += pickupChar(ASCII_SET)
        output += pickupChar(DIGITS) + pickupChar(DIGITS)
        output += pickupChar(SPEC_CHAR_SET)
    totalPossibilities=math.pow(len(ASCII_SET + DIGITS + SPEC_CHAR_SET), defaultLength)
    print(f"\nTotal number of possibilities : {totalPossibilities}") if showStats else 0
    print(f"{round(totalPossibilities/(1000*60*60*24*365*100), 1):,} centuries at 1000 try/second.\n")
    return ''.join(random.sample(output,len(output)))

def help():
    print("""
    PasswordGenerator
    Generate strong random password without annoying special chars such as \" or !
    
    Usage : 
        passwordGenerator.py [options]

        Options :
            -l <number>   Define length of the password
            --nospecials  Use only letters and digits
            -h, --help    Show this help
            -s, --stats   Show total number of possibilities 

        Without any options generates a 12 chars password including one special char
    """)

if __name__ == '__main__':
    args = sys.argv[1:]
    passLength = 12
    if "-l" in args:
        passLength=args[args.index("-l") + 1]
        try:
            passLength = int(passLength)
            if passLength < 8:
                print("\n    WARNING: Password length must be 8 or greater")
                exit()
        except:
            help()
            exit()
    if any(arg in ["-h","--help"] for arg in args):
        help()
        exit()
    if any(arg in ["-s","--stats"] for arg in args):
        showStats=True
    else:
        showStats=False

    if "--nospecials" in args:
        print(generatePass(includeSpecials=False, defaultLength=passLength, showStats=showStats))
    else:
        print(generatePass(defaultLength=passLength, showStats=showStats))
