import re

name = input ("Enter a file:")
hand = open (name,'r')
for line in hand:
    line = line.rstrip()
    str = re.findall('ab{3}',line)#str = re.findall('abbb',line)
    print (str)
