#check if a string ends with a word or interpuctions sign at the end

import regex as re

text1 = input('')
pattern = '.*([a-zA-Z]+|[\.|\?|\!|\,|\:|\;])$'
if re.search(pattern, text1):
    print('True')
else:
    print('False')