# Digits in the unicode space
import re
for i in range(32,10_000):
    ch = chr(i) # Character with the unicode if it is a digit
    if re.match('\d',ch):
        print(ch,end='')

print('')
'''In this program, we are looping over a range of unicode charcters with
the codepoints between 32 (space ) and 10,000. Each character is then tested
against a regular expression \d , which are also digits.'''
'''But digits in the unicode are far beyoud the ten familiar digits between
0 and 9.You can find more than 500 other chracters(with the codes above
10,000,too),Watch are also digits.'''
'''TO limit the regex to work only in the ASCII flag.'''
