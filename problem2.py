"""
##### Problem 2
Retrieve the contents of the sd.deltasd.bc.ca webpage.
Remove all of the HTML and display just the real contents of the page.
"""


import requests
import re

x = requests.get("https://sd.deltasd.bc.ca")
x = x.text.split(">")


x = re.sub("^((?!8230).)*$","",x)


print(x[0])