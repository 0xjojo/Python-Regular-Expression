import re
ip = input ("Enter your ip address:")
new_ip = re.sub('\.0*','.',ip)
print ("your ip address without leading zeros is:",new_ip)
#I use '\' to escape from '.' used as wild card
#'.' followed by '0' it's a  leading zero should be removed we put it in the secound
#place to keep it the we put the variable (ip address) in the third place
