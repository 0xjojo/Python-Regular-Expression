import re
string = input ("Enter a string:")
word = input ("Enter a word:")
words = re.findall(word,string)
for w in words:
    print (w)
