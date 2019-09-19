import re

name = input ("Enter a file:")
hand = open (name,'r')
for line in hand:
    line = line.rstrip()
    str = re.findall('[a-z]\S*_\S*[a-z]',line)
    print (str)
