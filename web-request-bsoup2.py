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
    # Based on structure of a random website with cheat sheets in <span> tags paginated
    # Modify as needed for appropriate structure
    # Get number of pages to parse through
    div = soup.find("div", {"class": "pagination"})
    span = div.find("span", {"class": "page_list"})
    pages = []
    for a in span:
        pages.append(a.text)
    titles = []
    # Parse through pages, scraping titles of cheat sheets
    for page in range(1, int(pages[len(pages) - 1])):
        r2 = requests.get(url + str(page), verify=False)
        soup2 = BeautifulSoup(r2.text, 'html.parser')
        div2 = soup2.find_all("div", {"class": "triptychdblr"})
        for div in div2:
            titles.append(div.find("span").string)
    print(titles)

if __name__=="__main__":
    # This is what happens if run as a script
    main()
else:
    # This is what happens if imported
    pass