#!/usr/bin/python -tt
# Basic cli wrapper for taking a URL and requesting it

import requests, sys

def usage():
    print("Usage: python[3] web-request-get.py <http[s]://www.example.com> [-r -R]")
    print("-r : Verbose request")
    print("-R : Verbose response")
    quit()

try:
    url = sys.argv[1]
except:
    usage()

if "-h" in sys.argv:
    usage()

if "-r" in sys.argv:
    verboseRequest = True
else:
    verboseRequest = False

if "-R" in sys.argv:
    verboseResponse = True
else:
    verboseResponse = False

def main():
    r = requests.get(url, verify=False)
    if verboseRequest:
        print("==Request==")
        print("=Headers=")
        print(r.request.headers)
        print()
    if verboseResponse:
        print("==Response==")
        print("=HTTP Code=")
        print(r.status_code)
        print()
        print("=Headers=")
        print(r.headers)
        print()
    print("=Body=")
    print(r.text)

if __name__=="__main__":
    # This is what happens if run as a script
    main()
else:
    # This is what happens if imported
    pass