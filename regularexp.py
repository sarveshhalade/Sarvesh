import re

s = 'Working out in GYM feels me alive'

match = re.search(r'GYM', s)

print('Start Index:', match.start())
print('End Index:', match.end())
