# Remove duplicates from a list
# and make sure the order is saved

data = [10,12,10,33,2,2,5,2]
result = []
values = set()
for i in data:
    if i not in values:
        values.add(i)
        result.append(i)

print(result)

""""Here's another technique to remove duplicates from a list. This time, we" \
make sure the order has been preserved.
Again,a set is used to check if the value was already seen, and a loop " \
scans the list from the left to right , taking the values which were not " \
seen, and a loop scans the from left to right, taking the values which,
were not seen yet."""
