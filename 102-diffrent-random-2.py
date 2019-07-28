  #Genrating a series
  # of *diffrent*random numbers

from random import randint  # firstly from random library we need to import rand-int module/package
data = set()  # here we declare a tuple , which can contain each value only once

while len(data) < 20:
    r = randint(0,100)
    data.add(r)

print(len(data))  # got 20 items
print(data)  # all difrent
