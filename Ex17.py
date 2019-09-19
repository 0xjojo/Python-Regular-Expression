import re
string = input("Enter a string:")
yes = re.findall('^.*[0-9]+$',string)
print (yes)
if len(yes) > 0 :
    print ("the string ends with a number")
else:
    print ("the string doesn't end with a number")
