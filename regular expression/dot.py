import re

string = "The quick brown fox jumps over the lazy dog."
pattern = r"brown.tiger"
pattern2 = r"brown.fox"


match = re.search(pattern, string)
if match:
    print("Match found!")
else:
    print("Match not found.")

print({match})


match2 = re.search(pattern2, string)
if match2:
    print("Match found!")
else:
    print("Match not found.")

print({match2})
