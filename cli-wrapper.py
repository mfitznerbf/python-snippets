#!/usr/bin/python -tt
# Basic cli wrapper for taking a single argument

import sys

try:
    argument = sys.argv[1]
except:
    print("No argument passed!")
    quit()

def someFunc():
    print(argument)

if __name__=="__main__":
    # This is what happens if run as a script
    someFunc()
else:
    # This is what happens if imported
    pass