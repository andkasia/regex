#find and print numbers only

import regex as re

str = input('')
results = re.findall('[0-9]+', str)
for match in results:
    print(match)