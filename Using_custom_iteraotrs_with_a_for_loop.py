# Using custom iterators with a "for" loop
class Count:
    def __init__(self,min,max):
        self.min = min
        self.max = max
    def __iter__(self):
        self.n = self.min - 1
        return self
    def __next__(self):
        if self.n == self.max:
            raise StopIteration
        self.n += 1
        return self.n

c = Count(10,15)
for i in c:  # using our iterator
    print(i)
#COMMENT :

# Iterators can be directly used in a "for" loop. In this example
# we are creating a class that can be used for counting objects.
# The object keeps its ranges, and returns an incrementing value each
# time "next" call is implicitly applied to it.

# The example demonstrates a trivial case of  incrementing integers,
# But you may think of a more complex behaviour.
