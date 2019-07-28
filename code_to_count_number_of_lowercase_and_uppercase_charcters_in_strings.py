string = input("Enter The string Here : ")
lower = 0
upper = 0

print(string)
for i in string:
    if(i.islower()):
        lower = lower+1
    elif(i.isupper()):
        upper = upper+1

print('Lowercase charcters : %s' % lower)
print('Upper character : %s' % upper)

