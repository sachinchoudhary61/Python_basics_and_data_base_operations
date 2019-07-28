# Generating and printing Fibonacci numbers below 100

a,b = 0,1

while a < 100:
    print(a)
    a,b = b, a+b

# Notice how nice is multiple assignment

# COMMENT:

"""
Let's solve a classical task of printing the first Fibonacci numbers.
In Python,you can effectively use tuple assignment and change the two
variable in a single line. Isn't that amazing?
"""
