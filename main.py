from bs4 import BeautifulSoup
from urllib.request import urlopen

InputURL = input("Please copy URL from website (starting with https): ") # For Test Example: https://www.nba.com/standings
OutputList = []

with urlopen(InputURL) as response:
    soup = BeautifulSoup(response, "html.parser")
    for anchor in soup.find_all("a"):
            hyperlink = anchor.get("href", "/")
            if hyperlink.index("/") != 0:
                  hyperlinkList = hyperlink.split()
                  for i in hyperlinkList:
                        OutputList.extend(hyperlinkList)
print(OutputList)
                  
"""
Comments:
So for the code above, it doesn't exactly take a list of URLs but it takes the user's input on a website.
I tried at first doing a list of user input of URLS but I just couldn't get it to work so I with a single input of a user entering a URL.
My thought process however for that though would be creating a for loop that takes the
range of how many URLS are inputted and then another for loop that filters through each URL and starts parsing the HTML and extracting
the hyperlinks out of those URLS. It kept throwing an error at me however so I went with a single URL.

The code above I used the terminal to download beautifulsoup4 (pip install beautifulsoup4)
BeautifulSoup4 is library that makes it so it scrapes other weblinks from web pages.

As an example above, I used https://www.nba.com/standings. 
I will say though for some other websites, I'm not too sure as to why it didn't want to run so this code totally doesn't work for every
website either.. but if you run it above with the website provided it should be okay.

But the code above takes NBA.com interface and takes all the hyperlinks and puts in all into one list.
This is the sample code that I used but edited it so it would be in a list.

#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen

with urlopen("https://en.wikipedia.org/wiki/Main_Page") as response:
    soup = BeautifulSoup(response, "html.parser")
    for anchor in soup.find_all("a"):
        print(anchor.get("href", "/"))


This is everything that I used and the thoughtout process behind it.
Again I'm sorry I didn't totally follow the rubric but this was something similar that I thought I could do.

"""

