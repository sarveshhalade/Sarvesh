import re

string = "Hello Raj!"
pattern = r"Raj!$"

match = re.search(pattern, string)
if match:
    print("Match found!")
else:
    print("Match not found.")
