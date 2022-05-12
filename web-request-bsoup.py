#!/usr/bin/python -tt
# Basic cli wrapper for taking a URL and requesting it, then parsing the response with regex to extract data

import requests, sys
from bs4 import BeautifulSoup

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

if len(sys.argv) < 2:
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
    soup = BeautifulSoup(r.text, 'html.parser')
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
    #print("=Body=")
    #print(r.text)
    print("=Match(es)=")
    # Based on structure of a random website with book titles in <a> tags each within <h1> tags
    # Modify as needed for appropriate structure
    h1s = soup.find_all("h1", {"class": "post-title"})
    for a in h1s:
        print(a.text)


if __name__=="__main__":
    # This is what happens if run as a script
    main()
else:
    # This is what happens if imported
    pass