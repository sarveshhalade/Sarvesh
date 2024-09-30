import re

s = 'Technical and non.Technical Knowledge is IMP'

match = re.search(r'.', s)
print(match)

match = re.search(r'\.', s)
print(match)

