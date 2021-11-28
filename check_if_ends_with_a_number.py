#check if ends with a number

import regex as re

text1 = input('')
pattern = '.*[0-9]+$'
if re.search(pattern, text1):
    print('True')
else:
    print('False')