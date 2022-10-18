#!/usr/bin/env python3

import random
import string
import sys

ASCII_SET = string.ascii_uppercase + string.ascii_lowercase
DIGITS = string.digits
SPEC_CHAR_SET = "&@#§+/$"

def pickupChar(charSet):
    return random.choice(charSet)

def generatePass(includeSpecials:bool = True, defaultLength: int = 12):
    output=""
    if not includeSpecials:
        for i in range(0, defaultLength):
            output += pickupChar(ASCII_SET + DIGITS)
    else:
        for i in range(0, defaultLength - 1):
            output += pickupChar(ASCII_SET + DIGITS)
        output += pickupChar(SPEC_CHAR_SET)
    return ''.join(random.sample(output,len(output)))

def help():
    print("""
    PasswordGenerator - © Romain Dudek 2022
    Generate strong random password without annoying special chars such as \" or !
    
    Usage : 
        passwordGenerator.py [options]

        Options :
            -l <number>   Define length of the password
            --nospecials  Use only letters and digits
            -h, --help    Show this help

        Without any options generates a 12 chars password including one special char
    """)

if __name__ == '__main__':
    args = sys.argv[1:]
    passLength = 12
    if "-l" in args:
        passLength=args[args.index("-l") + 1]
        try:
            passLength = int(passLength)
        except:
            help()
            exit()
    if any(arg in ["-h","--help"] for arg in args):
        help()
        exit()

    if "--nospecials" in args:
        print(generatePass(includeSpecials=False, defaultLength=passLength))
    else:
        print(generatePass(defaultLength=passLength))
