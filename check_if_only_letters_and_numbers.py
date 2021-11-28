#check whether a pattern contains only letters and numbers

import regex as re

text1 = input('')
pattern = '^([a-z]|[A-Z]|[0-9])+$'
if re.search(pattern, text1):
    print('True')
else:
    print('False')