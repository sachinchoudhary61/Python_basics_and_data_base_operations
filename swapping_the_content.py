# Swapping the content of the two variable

left = 'knife'
right = 'fork'
a = f'Before: {left},{right}'

print(a)

left,right = right,left

b = f'After:{left},{right}'
print(b)
