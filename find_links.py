# find all links

import regex as re

str = input('')
pattern = r'https:////[a-z0-9]*\.?[a-z]?[a-z]?\.?[a-z]?[a-z]?[a-z]?\.[a-z][a-z][a-z]?|http:////[a-z0-9]*\.?[a-z]?[a-z]?\.?[a-z]?[a-z]?[a-z]?\.[a-z][a-z][a-z]?'
results = re.findall(pattern,str)
print(results)