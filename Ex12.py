import re

name = input ("Enter a file:")
hand = open (name,'r')
for line in hand:
    line = line.rstrip()
    str = re.findall('.*z.*',line)
    print (str)
