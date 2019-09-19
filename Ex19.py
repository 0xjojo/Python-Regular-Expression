import re
string = input ("Enter a string:")
literals=[]
literal = 'a'
while len(literal) > 0 :
    literal = input ("Enter literals one by one press enter to quit:")
    literals.append(literal)
literals.pop()
for lit in literals :
    if re.search(lit,string,flags=1):
        print ("The word",lit,"exist")
    else :
        print("The word",lit,"doesn't exist")
