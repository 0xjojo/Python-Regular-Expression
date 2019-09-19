import re

name = input ("Enter a file:")
hand = open (name,'r')
for line in hand:
    line = line.rstrip()
    str = re.findall('^a.*$b\w',line)
    print (str)
