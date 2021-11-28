# find words with 3,4,5 letters

import regex as re

string = input('')
pattern = r'\b[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]?[a-zA-Z]?\b'

list1 = re.findall(pattern, string, re.IGNORECASE)
print(list1)