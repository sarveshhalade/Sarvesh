import re
regex = r'^The'
strings = ['The quick brown fox', 'The lazy dog', 'A quick brown fox','Rajvardhan is ']
for string in strings:
    if re.match(regex, string):
        print(f'Matched: {string}')
    else:
        print(f'Not matched: {string}')
