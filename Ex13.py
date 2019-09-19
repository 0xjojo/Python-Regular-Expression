import re

name = input ("Enter a file:")
hand = open (name,'r')
for line in hand:
    line = line.rstrip()
    str = re.findall('.+z.+',line)
    #str = re.findall('[a-zA-Z]+z[a-zA-Z]+',line)
    print (str)
