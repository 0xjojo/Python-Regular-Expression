import re

name = input ("Enter a file:")
hand = open (name,'r')
for line in hand:
    line = line.rstrip()
    str = re.findall('[a-zA-Z0-9_]+',line)
    print (str)
