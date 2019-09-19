import re
string = input ("Enter a string:")
word = input ("Enter a word:")
for w in  re.finditer(word,string):
    s = w.start()
    e = w.end()
    print (w,"exist located at",s,":",e)
