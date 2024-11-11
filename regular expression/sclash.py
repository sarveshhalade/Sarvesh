import re

s = 'geeks@forgeeks'

# without using \
match = re.search(r'.', s)
print(match)

# using \
match = re.search(r'\@', s)
print(match)
