
def f(x):
    return x ** 2
# create a list of squares
data = [ f(x) for x in range(10)]
# print the content of "data"
for x in range(10):
    print(f'{x}^2 = {data[x]}')


