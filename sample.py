import re


text = "This is a test and there are several things we are looking for"

text = re.sub("[^(?!.*a\w+\s)]","_",text)

print(text)

