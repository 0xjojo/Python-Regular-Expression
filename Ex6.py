import re

name = input ("Enter a file:")
hand = open (name,'r')
for line in hand:
    line = line.rstrip()
    str = re.findall('ab{2,3}',line)
    print (str)
