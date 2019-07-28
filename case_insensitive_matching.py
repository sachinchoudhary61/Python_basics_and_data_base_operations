# case-insensitive matching
# with regular expressions

import re
str = ['Word','word','woRD','Hi']
for s in str:
    print('TESTING'+ s +'...',end = '')

    if re.match('word',s,re.IGNORECASE): # add this flag
        print('OK')
    else:
        print('Not OK')
