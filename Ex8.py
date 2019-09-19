import re

name = input ("Enter a file:")
hand = open (name,'r')
for line in hand:
    line = line.rstrip()
    str = re.findall('[A-Z]{1}}_\S+[a-z]',line)
    print (str)
