import re

s = 'Dr D Y Patil College of Engineering Kolhapur '

match = re.search(r'College', s)

print('Start Index:', match.start())
print('End Index:', match.end())
