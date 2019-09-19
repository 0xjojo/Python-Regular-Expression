import re
string = input ("Enter a string:")
nums = re.findall('[0-9]{1,3}',string)
for n in nums:
    print (n)
