# using regular expressions
# to extract a number from string

import re

str = 'On the 14th floor'

# want 14 to extract out from the string

match = re.search('\d+', str)

# \d = digit
# \d+ = one or more digits

if match:
    print(match[0])
#match[0]=what was matched

