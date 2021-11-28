#find number of patters

import regex as re

a = input('')
pattern = input('')

print(len(re.findall(pattern, a)))
