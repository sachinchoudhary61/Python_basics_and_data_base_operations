# genrating a series
# of *diffrent* random numbers

from random import randint

data = set()
n = 0

while n < 1:
    r = randint(0,100000)
    if r not in data:
        n = n+1
        data.add(r)  # new number


print(len(data))  # got 20 items
print(data)  # all different
