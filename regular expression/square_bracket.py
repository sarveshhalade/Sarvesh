import re

string = "The quick brown fox jumps over the lazy dog"
pattern = "[a-e]"
pattern2 = "[^a-m]"
result = re.findall(pattern, string)
result2 = re.findall(pattern2, string)

print(result) 
print(result2)