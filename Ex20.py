import re
string = input ("Enter a string:")
literals=[]
literal = 'a'
while len(literal) > 0 :
    literal = input ("Enter literals one by one press enter to quit:")
    literals.append(literal)
literals.pop()
for lit in literals:
    for l in re.finditer(lit,string):
        s = l.start()
        e = l.end()
        print (l,"exist located at",s,":",e)
